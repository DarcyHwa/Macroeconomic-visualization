import streamlit as st

import pandas as pd
import plotly.graph_objects as go



# 读取 CSV 文件
df1 = pd.read_csv('assets/CPI-A2.csv', encoding='utf-8')

# 创建一个空的图形对象
fig1 = go.Figure()

# 添加第一条折线（CPI环比），突出显示每个数据点
fig1.add_trace(go.Scatter(
    x=df1['月份'],
    y=df1['CPI环比'],
    mode='lines+markers',  # 绘制线条和标记
    name='CPI环比',
    line=dict(color='#00ffa1'),  # 设置线条颜色
    marker=dict(color='#00ffa1', size=8)  # 设置标记的颜色和大小
))

# 添加第二条折线（CPI同比），突出显示每个数据点
fig1.add_trace(go.Scatter(
    x=df1['月份'],
    y=df1['CPI同比'],
    mode='lines+markers',  # 绘制线条和标记
    name='CPI同比',
    line=dict(color='#00cdff'),  # 设置线条颜色
    marker=dict(color='#00cdff', size=8)  # 设置标记的颜色和大小
))
# 添加中轴线 y=100 的黑色虚线
fig1.add_trace(go.Scatter(
    x=df1['月份'],
    y=[100] * len(df1),  # 创建一个长度和x轴相同，值为100的列表
    mode='lines',
    name='荣枯线',
    line=dict(color='black', dash='dash')  # 设置线条为黑色虚线
))

# 更新图表的布局
fig1.update_layout(
    title='CPI环比与同比变化趋势',
    xaxis_title='月份',
    yaxis_title='CPI值',
    legend_title='CPI指标',
    title_x=0.4
)


# 显示图形
# fig1.show()


@st.cache_data
def CPI_1():
    st.title('消费价格指数CPI')

    # st.write('这是内容')

    st.plotly_chart(fig1, use_container_width=True)

#CPI_1()