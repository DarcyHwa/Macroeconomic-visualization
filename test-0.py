import streamlit as st
from streamlit_echarts import st_echarts
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import pandas as pd
import numpy as np

# st.markdown(" <style>iframe{ height: 300px !important } ", unsafe_allow_html=True)


# 设置全局属性
st.set_page_config(
    page_title='标题',
    page_icon=' ',
    layout='wide'
)

## st.sidebar 下的内容会被渲染到侧边栏
with st.sidebar:
    st.title('欢迎来到我的应用')
    st.markdown('---')
    st.markdown('这是它的特性：\n- feature 1\n- feature 2\n- feature 3')

## 默认渲染到主界面
st.title('界面标题')
st.markdown('### markdown 三级标题')
st.write('这是一个普通的文本块')
st.info('这是主界面内容')

#
#
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')
#
# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
#
# st.markdown('---')
# col1, col2 = st.columns([3, 1])
# data = np.random.randn(10, 1)
#
# col1.subheader("A wide column with a chart")
# col1.line_chart(data)
#
# col2.subheader("A narrow column with the data")
# col2.write(data)
#
# st.markdown('---')

