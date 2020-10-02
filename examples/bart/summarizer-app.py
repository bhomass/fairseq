#!/usr/bin/env python
# coding: utf-8

# In[9]:
import sys
sys.path.insert(0,'../..')

import pandas as pd

import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput, TextAreaInput, HTMLTemplateFormatter
from bokeh.plotting import figure

from bokeh.io import show, output_notebook#, output_file


# In[3]:


# output_notebook()


# In[20]:


from datetime import date
from random import randint

from bokeh.io import show
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn
from bokeh.models import Button, Column

from bokeh.models.widgets import Div
from bokeh.layouts import column

from summarizer_infer import Summarizer
# output_file("layout.html")

text = TextAreaInput(title="Input Text", value='Enter Text to summarize', rows=20, cols=20, max_length=10000)
button = Button(label="Summarize", button_type="success")
inputs = Column(text, button, width=400)

print('instantiating summarizer')
summarizer = Summarizer()
print('summarizer initiated')

# summary_df = summarizer.summarize(source_text)

lines = [{'cnn_summary': 'cnn_summary', 'xsum_summary': 'xsum_summary'}]
summary_df = pd.DataFrame(lines)

Columns = [TableColumn(field=Ci, title=Ci, width=360, formatter=HTMLTemplateFormatter(template='<div style="width: 340px;word-break: break-all;white-space: normal;"><%= value %></div>')) for Ci in summary_df.columns] # bokeh columns
# columns = [
#     TableColumn(field='atomic number', title='Atomic Number'),
#     TableColumn(field='symbol', title='Symbol'),
#     TableColumn(field='name', title='Name', 
#                 formatter=HTMLTemplateFormatter(template='<font color="<%= CPK %>"><%= value %></font>'))
# ]
columnDataSource = ColumnDataSource(summary_df)
data_table = DataTable(columns=Columns, source=columnDataSource, row_height=400, width=740) # bokeh table

# show(data_table)
div = Div(text="""The Summary of your statement is given below. Results are given by CNN and XSum models.""",
width=800, height=20)

# show(data_table)

column = column(div, data_table)
def update_title():
    print('button clicked')
    source = text.value
#     div.text = source
    print('calling summarizer')
    summary_df = summarize(source)
    print('update columnDataSource')
    columnDataSource.data = summary_df
    

button.on_click(update_title)

# show(row(inputs, column, width=800))
curdoc().add_root(row(inputs, column, width=800))
curdoc().title = "Summarizer"

# In[ ]:

def summarize(source):
    print('calling summarizer to summarize')
    summary_df = summarizer.summarize(source)
    
    return summary_df




