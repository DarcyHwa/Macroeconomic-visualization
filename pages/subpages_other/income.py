import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

# 加载 GeoJSON 数据
geojson_path = 'assets/China2.geoJson'
with open(geojson_path, 'r', encoding='utf-8') as file:
    china_geojson = json.load(file)

# 提取省份名称并为每个省份生成随机的人均收入数据
province_names = [feature['properties']['name'] for feature in china_geojson['features']]
random_income = np.random.randint(20000, 100000, size=len(province_names))

# 创建新的 DataFrame 包含省份名称和对应的人均收入
income_data = pd.DataFrame({
    "Province": province_names,
    "Income": random_income
})

# 创建 Choropleth 图层
trace = go.Choropleth(
    geojson=china_geojson,
    locations=income_data['Province'],
    z=income_data['Income'],
    featureidkey="properties.name",
    colorscale="Viridis",
    marker_line_color='peachpuff',  # 设置省份边界颜色
    colorbar_title="Average Income"
)

# 创建布局
layout = go.Layout(
    title=go.layout.Title(
        text="2023年各地区人均可支配收入",
        x=0.35,  # 标题居中

    ),
    geo=dict(
        scope='asia',  # 限制地图范围为亚洲
        showframe=False,
        projection_scale=1.8,  # 放大比例
        showcoastlines=False,
        showcountries=False,
        showland=False,
        showlakes=False,
        projection_type='mercator',
        center=dict(lat=38, lon=105),  # 中心点坐标
        landcolor='white',
        lakecolor='white',
        subunitcolor="peachpuff"
    ),
    margin=dict(l=0, r=0, t=30, b=0),  # 减小图表边距
    paper_bgcolor='rgba(0,0,0,0)',  # 设置图表背景透明
    plot_bgcolor='rgba(0,0,0,0)',  # 设置绘图区域背景透明
    height=650,
)

# 组合图层和布局
fig = go.Figure(data=[trace], layout=layout)


# 显示地图
# fig.show()



@st.cache_data
def income_1():
    st.title('人均可支配收入')
    #st.write('这是内容')



    st.plotly_chart(fig, use_container_width=True)