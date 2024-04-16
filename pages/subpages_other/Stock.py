import streamlit as st
import akshare as ak
import plotly.graph_objs as go
import plotly.subplots as sp
import pandas as pd

# 获取上证指数的贪婪曲线数据
index_fear_greed_funddb_df = ak.index_fear_greed_funddb(symbol="上证指数")

# 转换日期格式
index_fear_greed_funddb_df['date'] = pd.to_datetime(index_fear_greed_funddb_df['date'])

# 筛选2024-01-01到今天的数据
start_date = '2024-01-01'
end_date = pd.to_datetime('today').strftime('%Y-%m-%d')
filtered_df = index_fear_greed_funddb_df[
    (index_fear_greed_funddb_df['date'] >= start_date) & (index_fear_greed_funddb_df['date'] <= end_date)]

# 创建filtered_df的深拷贝
filtered_df_copy = filtered_df.copy()

# 计算恐惧和贪婪值
filtered_df_copy['fear_value'] = filtered_df_copy.apply(lambda x: 50 - x['fear'] if x['fear'] < 50 else 0, axis=1)
filtered_df_copy['greed_value'] = filtered_df_copy.apply(lambda x: x['fear'] - 50 if x['fear'] > 50 else 0, axis=1)

# 创建带有两个子图的图表
fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                       subplot_titles=('恐惧贪婪指数', '收盘价'))

# 在第一个子图中添加反向的恐惧指数柱形图
fig.add_trace(
    go.Bar(x=filtered_df_copy['date'], y=-filtered_df_copy['fear_value'], name='恐惧', marker_color='red'), row=1,
    col=1)

# 在第一个子图中添加贪婪指数柱形图
fig.add_trace(
    go.Bar(x=filtered_df_copy['date'], y=filtered_df_copy['greed_value'], name='贪婪', marker_color='green'), row=1,
    col=1)

# 更新恐惧贪婪指数子图的 y 轴范围和标题
fig.update_yaxes(range=[-50, 50], row=1, col=1, title_text='恐惧 <--> 贪婪')

# 3000点保卫线
fig.add_trace(
    go.Scatter(x=[filtered_df['date'].iloc[0], filtered_df['date'].iloc[-1]], y=[3000, 3000], mode='lines',
               name='参考线', line=dict(color='gray', dash='dot')), row=2, col=1)
fig.add_annotation(x=filtered_df['date'].iloc[-1], y=3000, text='3000点参考线', font=dict(color='#636EFB', size=14),
                   showarrow=False, row=2, col=1)

# 在第二个子图中添加收盘价折线
fig.add_trace(go.Scatter(x=filtered_df['date'], y=filtered_df['index'].round(2), mode='lines', name='收盘价',
                         line=dict(color='#ED1716')), row=2, col=1)

# 设置图表布局
fig.update_layout(title='大盘估值情绪与收盘价 ｜ 2024-01-01 至今',
                  title_font=dict(size=32, family="Arial", color="#888"), title_x=0.3, height=600, showlegend=True)

# fig.show()

@st.cache_data
def Stock_1():
    st.title('股市行情')
    # st.write('这是内容')


    st.plotly_chart(fig, use_container_width=True)

#stock_1()
