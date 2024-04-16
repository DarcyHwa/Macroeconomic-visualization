import streamlit as st
from pages.subpages_finance.money import money_1


# def Other_Data():
#     st.title('其他数据页')
#     st.write('这是内容')


# 使用Session State跟踪当前页面
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'money_1'

# 定义一个函数来切换页面
def switch_page(page_name):
    st.session_state.current_page = page_name

# 在侧边栏使用按钮来切换页面3
with st.sidebar:

    if st.button('货币供应量'):
        switch_page('money_1')
    if st.button('社会融资规模'):
        switch_page('money_1')
    if st.button('外汇和黄金储备'):
        switch_page('money_1')
    if st.button('新增信贷'):
        switch_page('money_1')


# # 根据当前页面渲染相应的页面内容
# if st.session_state.current_page == 'Consumer_Data':
#     Consumer_Data()

if st.session_state.current_page == 'money_1':
    money_1()

elif st.session_state.current_page == 'money_1':
    money_1()

# elif st.session_state.current_page == 'page4':
#     page4_app()
else:
    money_1()
