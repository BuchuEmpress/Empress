
import streamlit as st 

# this reads the markdown file with encoding specified
with open ('new_file.md', 'r', encoding='utf-8', errors='ignore') as file:
    markdown_content = file.read()
    # displays the markdown content
st.markdown(markdown_content)

# readind an md file is different frm text; reason for the "encoding='utf-8" because most markdown files are encodied in utf-8. you have to 
# specify the the encoding when opening the file else it gives you a decoding error