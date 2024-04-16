import streamlit as st

import pandas as pd
import plotly.graph_objs as go


# Load the data from the CSV file
data = pd.read_csv('assets/社零增速环比2.csv')  # 替换 'your_file_path.csv' 为您的文件路径

horizontal_bar_chart = go.Figure(
    data=[
        go.Bar(
            y=data['月份'],  # y-axis has the months
            x=data['社零环比'],  # x-axis has the retail growth rates
            orientation='h',  # Orientation is horizontal
            #marker=dict(color='orange'),  # Bars will be colored green
        )
    ]
)

# Update layout for the chart
horizontal_bar_chart.update_layout(
    title="社会零售环比增速",
    xaxis_title="环比增速 (%)",
    yaxis_title="月份",
    xaxis=dict(
        side='top'  # Moves the x-axis to the top, which will appear on the right in a horizontal bar chart
    ),
    template="plotly_white",
    title_x=0.3,
    # width=500
)

# Display the horizontal bar chart
# horizontal_bar_chart.show()



@st.cache_data
def sheling_1():
    st.title('社会消费品零售总额')
    # st.write('这是内容')

    st.plotly_chart(horizontal_bar_chart, use_container_width=True)
