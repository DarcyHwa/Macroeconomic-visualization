import streamlit as st
from pages.subpages_other.Stock import Stock_1
from pages.subpages_other.income import income_1

def Other_Data():
    st.title('其他数据页')
    st.write('这是内容')
    # 在这里添加更多的Streamlit调用来构建你的页面2






#Consumer_Data()

# 使用Session State跟踪当前页面
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'income_1'

# 定义一个函数来切换页面
def switch_page(page_name):
    st.session_state.current_page = page_name

# 在侧边栏使用按钮来切换页面3
with st.sidebar:

    if st.button('人均收入'):
        switch_page('income_1')
    if st.button('股市行情'):
        switch_page('Stock_1')
    if st.button('进出口规模'):
        switch_page('income_1')
    if st.button('资产投资'):
        switch_page('income_1')


# # 根据当前页面渲染相应的页面内容
# if st.session_state.current_page == 'Consumer_Data':
#     Consumer_Data()

if st.session_state.current_page == 'Stock_1':
    Stock_1()

elif st.session_state.current_page == 'income_1':
    income_1()

# elif st.session_state.current_page == 'page4':
#     page4_app()
else:
    income_1()
