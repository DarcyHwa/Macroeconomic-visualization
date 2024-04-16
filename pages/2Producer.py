import streamlit as st
from pages.subpages_producer.PMI import PMI_1


# def Other_Data():
#     st.title('其他数据页')
#     st.write('这是内容')


# 使用Session State跟踪当前页面
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'PMI_1'

# 定义一个函数来切换页面
def switch_page(page_name):
    st.session_state.current_page = page_name

# 在侧边栏使用按钮来切换页面3
with st.sidebar:

    if st.button('采购经理指数PMI'):
        switch_page('PMI_1')
    if st.button('生产者出厂价格指数PPI'):
        switch_page('PMI_1')
    if st.button('工业增加值'):
        switch_page('PMI_1')


# # 根据当前页面渲染相应的页面内容
# if st.session_state.current_page == 'Consumer_Data':
#     Consumer_Data()

if st.session_state.current_page == 'PMI_1':
    PMI_1()

elif st.session_state.current_page == 'income_1':
    PMI_1()

# elif st.session_state.current_page == 'page4':
#     page4_app()
else:
    PMI_1()
