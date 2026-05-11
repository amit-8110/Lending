'''
user: home page!
'''
import numpy as np
import pandas as pd
from numpy.random import default_rng as rng
import streamlit as st
from envelop import Envelop, Style
from envelop.ui import Text, MathExp, DataFrame, Div, Link, SideBar, Table
from envelop.chart import AreaChart



# st.set_page_config(
#     page_title='app' or __file__,
#     layout="wide",
# )

env = Envelop(title='lending')


Text('new testing', style=Style(color='red', font_size='25px'))
    


import requests as r



def get_tr(ids):
    return r.get(f'http://127.0.0.1:8000/api/v1/tr/{ids}').json()


ids = st.text_input('Transaction ids:')

if st.button('Search') and ids != None:
    data = get_tr(ids=ids)
    
    DataFrame(data)





# Text('hi there')

# MathExp(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
# ''')


# df = pd.DataFrame(
#     {
#         "col1": list(range(20)) * 3,
#         "col2": rng(0).standard_normal(60),
#         "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
#     }
# )

# DataFrame(df)


# st.line_chart(df, x='col1', y='col2', color='col3', x_label='new')

# AreaChart(df, x_='col1', y_='col2', color='col3')


