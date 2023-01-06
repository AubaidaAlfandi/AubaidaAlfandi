import streamlit
from PIL import Image

streamlit.set_page_config(page_title="paragraph", page_icon=" :tada:", layout="wide" )

pic1 = Image.open("/lab.png")

with streamlit.container():
  streamlit.subheader("hi , i am aubaida :wave:")
  streamlit.title("programmer from syria")
  streamlit.write("i am passionate about programming and gaming , now i am trying to find some new moduels of python like streamlit")


with streamlit.container():
  l_c, r_c =streamlit.columns(2)
  with l_c:
    streamlit.write("---")
    streamlit.subheader("what i do ?.")
    streamlit.write("i am currently full time student at college of petrochemical engineering in al-furat university in deir ezzor, syria and i am learning new ways to to expand my skills in python language and video game development. ")
  with r_c:
    streamlit.image(pic1)
