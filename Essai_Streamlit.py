import streamlit as st

st.write("## Test test")

st.slider('Direction d''arrivée',min_value=0,max_value=1,step=0,1)

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
st.caption('This is a small text')

st.sidebar.header("About")
