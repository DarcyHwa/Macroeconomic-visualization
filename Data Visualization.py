import streamlit as st

# st.markdown(" <style>iframe{ height: 300px !important } ", unsafe_allow_html=True)
# 设置页面配置
st.set_page_config(page_title='Data Visualization', layout='wide')


st.title('经济数据可视化-首页')
st.markdown('### markdown 三级标题')

st.info('这是info内容')
st.write('这是一个普通的文本块')


with st.sidebar:
    #页面链接
    st.page_link("Data Visualization.py", label="可视化首页", icon="🏠")
    st.page_link("pages/1Consumer.py", label="消费数据", icon="😎")
    st.page_link("pages/2Producer.py", label="生产数据", icon="🥲")
    st.page_link("pages/3Finance.py", label="金融数据", icon="😏")
    st.page_link("pages/Other.py", label="其他数据", icon="🤡")