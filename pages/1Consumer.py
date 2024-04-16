import streamlit as st
from pages.subpages_consumer.CPI import CPI_1
from pages.subpages_consumer.sheling import sheling_1

#
# def Consumer_Data():
#     st.title('消费数据页')
#     st.write('这是内容')
#     # 在这里添加更多的Streamlit调用来构建你的页面2
#
# #Consumer_Data()

# 使用Session State跟踪当前页面
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'CPI_1'


# 定义一个函数来切换页面
def switch_page(page_name):
    st.session_state.current_page = page_name


# 在侧边栏使用按钮来切换页面3
with st.sidebar:
    if st.button('消费者价格指数CPI'):
        switch_page('CPI_1')
    if st.button('社会消费品零售总额'):
        switch_page('sheling_1')

    if st.button('企业商品价格指数'):
        switch_page('page3')
    if st.button('消费者信息指数'):
        switch_page('page4')

# # 根据当前页面渲染相应的页面内容
# if st.session_state.current_page == 'Consumer_Data':
#     Consumer_Data()

if st.session_state.current_page == 'CPI_1':
    CPI_1()

elif st.session_state.current_page == 'sheling_1':
    sheling_1()

# elif st.session_state.current_page == 'page4':
#     page4_app()
else:
    CPI_1()
