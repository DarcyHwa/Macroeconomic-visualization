import streamlit as st
from page1 import app as page1_app
from page2 import app as page2_app
from page3 import app as page3_app
from page4 import app as page4_app
from page5 import app as page5_app
from page6 import app as page6_app

# st.markdown(" <style>iframe{ height: 300px !important } ", unsafe_allow_html=True)
# 设置页面配置
st.set_page_config(page_title='Data Visualization', layout='wide')

# 使用Session State跟踪当前页面
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'page1'

# 定义一个函数来切换页面
def switch_page(page_name):
    st.session_state.current_page = page_name

# 在侧边栏使用按钮来切换页面
with st.sidebar:
    st.write("经济数据可视化")
 
    if st.button('可视化首页'):
        switch_page('page1')
    if st.button('生产数据页'):
        switch_page('page2')
    if st.button('消费数据页'):
        switch_page('page3')
    if st.button('金融数据页'):
        switch_page('page4')
    if st.button('其他数据页'):
        switch_page('page5')
    if st.button('数据测试页'):
        switch_page('page6')


# 根据当前页面渲染相应的页面内容
if st.session_state.current_page == 'page1':
    page1_app()
elif st.session_state.current_page == 'page2':
    page2_app()
elif st.session_state.current_page == 'page3':
    page3_app()
elif st.session_state.current_page == 'page4':
    page4_app()
elif st.session_state.current_page == 'page5':
    page5_app()
elif st.session_state.current_page == 'page6':
    page6_app()
else:
    page1_app()

