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
from Christiaan.TechnologyALgo.techFinder import getTechRecommendations
from bokeh.models.widgets import Slider
from functools import partial
from bokeh.events import ButtonClick
from bokeh.client import push_session
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from datetime import date
from random import randint
from bokeh.models.widgets import Select


def getRecommendedTechnologies(data_table,dropdown,mentorSlider,extraSlider):

    print('dropdown',dropdown.value)
    print('mentorSlider',mentorSlider.value)
    print('extraSlider',extraSlider.value)

    columns = [
    TableColumn(field="tech", title="Recommended technology course"),
    TableColumn(field="mentor", title="Mentor/extra"),
            ]
    data_table.columns = columns

    data_table.source = ColumnDataSource(dict(
        tech=['tech1','tech2'],
        mentor=['m','V'],
            ))
    return None


def mainscreen():
    session = push_session(curdoc())
    #BDAEmployees = getTechRecommendations()


    #employees = [('BDA','BDA'),None]+[(str(employee.Fname)+' '+str(employee.Lname),str(employee.employeeID)) for employee in BDAEmployees]
    #menu = employees




    #enu=[('A','B')]
    #dropdown = Dropdown(label="Select Employee to train", button_type="warning", menu=menu)

    selectEmployee = Select(title="Trainee:", value="foo", options=["foo", "bar", "baz", "quux"])


    mentorSlider = Slider(start=0, end=10, value=1, step=1, title="Number of mentor technologies")
    extraSlider = Slider(start=0, end=10, value=1, step=1, title="Number of extra technologies")

    buttonGetRecommendedCourses=Button(label="Get recommended tech courses", button_type="success")

    data = dict(
        tech=[' ']*15,
        mentor=[' ']*15,
            )

    source = ColumnDataSource(data)

    columns = [
    TableColumn(field="tech", title="Recommended technology course"),
    TableColumn(field="mentor", title="Mentor/extra"),
            ]
    data_table = DataTable(source=source, columns=columns, width=400, height=280)


    divMentor = Div(text="---Suggested Mentor: ")
    divMentor2 = Div(text="",width=20)



    buttonGetRecommendedCourses.on_click(partial(getRecommendedTechnologies,data_table,selectEmployee,mentorSlider,extraSlider))
    #buttonGetRecommendedCourses.on_event(ButtonClick, getRecommendedTechnologies)

    #show(column(dropdown,slider,extraSlider,buttonGetRecommendedCourses))





    session.show(row(column(selectEmployee,mentorSlider,extraSlider,buttonGetRecommendedCourses),data_table,divMentor2,divMentor))
    session.loop_until_closed()


mainscreen()
