import streamlit as st
from PIL import Image
import pandas as pd

aa = './.streamlit/logo.png'
image = Image.open(aa)
st.set_page_config(
    page_title="宮野沢変電所 重点監視サイト", 
    page_icon=image, 
    layout="centered", 
    initial_sidebar_state="auto", 
    )

st.title('宮の沢変電所 重点監視サイト')

li = (['あ','capture1.png'], ['い','capture2.png'], ['う','capture3.png'])

l2 = []
for i in range(0,3):
    a = li[i][0]
    print(li[i][0])
    l2.append(a)

what_lang = st.selectbox('カメラを選択してください', l2)

for i in range(0,3):
    if what_lang == li[i][0]:
        aa = li[i][1]

st.text(aa)
image = Image.open(aa)
st.image(image, use_column_width=True)


st.subheader('外温チャート')
df = pd.read_csv('temp.csv', index_col='日付')

st.line_chart(df)
st.dataframe(df)