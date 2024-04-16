import streamlit as st

import pandas as pd
import plotly.graph_objects as go



# Load your data
data = pd.read_csv('assets/PMI_2.csv')

# Create a figure
fig = go.Figure()

# Add traces for PMI values
fig.add_trace(go.Scatter(
    x=data['月份'], y=data['制造业PMI'],
    mode='lines',
    line_shape='hv',
    line_color='blue',
    name='制造业PMI'
))
fig.add_trace(go.Scatter(
    x=data['月份'], y=data['非制造业PMI'],
    mode='lines',
    line_shape='hv',
    line_color='red',
    name='非制造业PMI'
))

# Add a horizontal line at y=50 to represent the boom-bust threshold
fig.add_shape(type="line",
              x0=data['月份'].min(), y0=50, x1=data['月份'].max(), y1=50,
              line=dict(color="Gray", width=2, dash="dash"))

# Add a fake trace for legend purpose
fig.add_trace(go.Scatter(
    x=[None], y=[None],  # No actual data points
    mode='lines',
    line=dict(color="Gray", width=2, dash="dash"),
    name='荣枯线'
))

# Update layout
fig.update_layout(
    title='制造业和非制造业 PMI',
    xaxis_title='月份',
    yaxis_title='PMI 值',
    showlegend=True,
    title_x = 0.4
)

# Display the figure
#fig.show()

@st.cache_data
def PMI_1():
    st.title('采购经理指数PMI')

    # st.write('这是内容')

    st.plotly_chart(fig, use_container_width=True)

#CPI_1()