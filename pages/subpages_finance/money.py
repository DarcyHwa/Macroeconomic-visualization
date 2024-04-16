import streamlit as st

import pandas as pd
import plotly.graph_objects as go



import pandas as pd
import plotly.graph_objs as go

# Load your data
data = pd.read_csv('assets/货币供应2.csv')

# 准备绘图数据
x = data['月份']
y1 = data['货币(M1)_期余-亿元']
y2 = data['准货币(M2-M1)_期余-亿元']

# 创建堆叠面积图
fig = go.Figure()

# 添加货币(M1)数据
fig.add_trace(go.Scatter(
    x=x, y=y1,
    mode='lines',
    name='货币(M1)',
    stackgroup='one',  # 定义为同一堆叠组
    line=dict(width=0.5, color='blue'),
    fill='tonexty'  # 填充到下一个Y值
))

# 添加准货币(M2-M1)数据
fig.add_trace(go.Scatter(
    x=x, y=y2,
    mode='lines',
    name='准货币(M2-M1)',
    stackgroup='one',
    line=dict(width=0.5, color='red'),
    fill='tonexty'
))

# 更新布局，增加标题和坐标轴标签
fig.update_layout(
    title='货币(M1) 和 准货币(M2-M1) 流动',
    xaxis_title='月份',
    yaxis_title='货币供应量 (亿元)',
    showlegend=True,
    title_x=0.35,
    height=650
)


# 显示图表
# fig.show()


@st.cache_data
def money_1():
    st.title('货币供应量')
    st.info('M2-M1 增加表示货币流动性降低,人民更多把钱存储在银行,而不是用于消费或投资')

    st.plotly_chart(fig, use_container_width=True)

#CPI_1()