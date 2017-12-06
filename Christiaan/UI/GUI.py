__author__ = 'christiaan'
# encoding=utf8
# -*- coding: utf-8 -*-
import sys


from bokeh.layouts import row, column, layout
from bokeh.models.widgets import CheckboxGroup
from bokeh.models import Button
from bokeh.plotting import figure, curdoc
from bokeh.models.widgets import Div
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown
from  Christiaan.Facades import EnginesFacade
from Christiaan.Engines import LinProgEngine
from bokeh.models.widgets import Slider
from functools import partial
from bokeh.events import ButtonClick
from bokeh.client import push_session
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from datetime import date
from random import randint
from bokeh.models.widgets import Select
from bokeh.models import NumberFormatter


def getRecommendedTechnologies(employees,data_table,dropdown,mentorSlider,extraSlider,divmentor,divCost,divPractice):

    eFname = dropdown.value.split(' ',1)[0]
    eLname = dropdown.value.split(' ',1)[1]


    employeeObjectList = [employee for employee in employees if (employee.lName==eLname and employee.fName==eFname)]
    assert len(employeeObjectList)==1
    selectedEmployee = employeeObjectList[0]

    solution,estTotalCost= EnginesFacade.getRecommendedTrainingsForEmployee(selectedEmployee,mentorSlider.value,extraSlider.value)

    techs=[item[0] for item in solution]
    costs=[item[1] for item in solution]
    weights=[item[2] for item in solution]
    mentors = [item[3] for item in solution]


    data_table.source.data = dict(
        tech=techs,
        mentor=mentors,
        cost=costs,
        importance=weights
            )

    divmentor.text="<b>  Suggested mentor:</b> "+str(selectedEmployee.mostSimilarMentor.fName) +' '+str(selectedEmployee.mostSimilarMentor.lName)
    divCost.text="<b> Total estimated cost:</b> "+str(estTotalCost)+" euro"
    divPractice.text="<b>  Practice:</b> "+selectedEmployee.practice



def mainscreen():
    session = push_session(curdoc())
    allEmployees = EnginesFacade.getAllTrainees(['BI','BD&A'])



    employeeNames = sorted([str(employee.fName)+' '+str(employee.lName) for employee in allEmployees])
    selectEmployee = Select(title="Trainee:", value=employeeNames[0], options=employeeNames)


    mentorSlider = Slider(start=1, end=10, value=5, step=1, title="Number of mentor technologies")
    extraSlider = Slider(start=1, end=10, value=2, step=1, title="Number of extra technologies")

    buttonGetRecommendedCourses=Button(label="Get recommended tech courses", button_type="success")

    listLen=0
    data = dict(
        tech=[' ']*listLen,
        mentor=[' ']*listLen,
        cost=[' ']*listLen,
        importance=[' ']*listLen
            )




    source = ColumnDataSource(data)
    percentageformatter = NumberFormatter(format='0%')
    columns = [
    TableColumn(field="tech", title="Technology course"),
    TableColumn(field="mentor", title="Mentor selection"),
    TableColumn(field="cost", title="Est. Cost (Euro)"),
    TableColumn(field="importance", title="Market importance",formatter=percentageformatter)
            ]
    data_table = DataTable(source=source, columns=columns, width=600, height=280)

    divPractice = Div(text="<b>  Practice:</b> ")
    divMentor = Div(text="<b>  Suggested mentor:</b> ")
    divCostEst = Div(text="<b> Total estimated cost:</b> ")



    buttonGetRecommendedCourses.on_click(partial(getRecommendedTechnologies,allEmployees,data_table,selectEmployee,mentorSlider,extraSlider,divMentor,divCostEst,divPractice))

    session.show(row(column(selectEmployee,mentorSlider,extraSlider,buttonGetRecommendedCourses),data_table,column(divPractice,divMentor,divCostEst)))
    session.loop_until_closed()


mainscreen()


