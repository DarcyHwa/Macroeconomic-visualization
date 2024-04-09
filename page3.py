import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


def app():
    st.title('消费数据页')
    st.write('这是内容')
    # 在这里添加更多的Streamlit调用来构建你的页面2

    b = (
        Bar()
        .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
        .add_yaxis(
            "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
            ),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    st_pyecharts(b)
