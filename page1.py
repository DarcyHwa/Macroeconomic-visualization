import streamlit as st
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from streamlit_echarts import st_pyecharts


def app():
    st.title('经济数据可视化')
    st.write('这是内容')
    # 在这里添加更多的Streamlit调用来构建你的页面1

    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
    )
    st_pyecharts(c)
