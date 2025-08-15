# import streamlit as st
# # # # st.title("My Gen AI")


# # print("run")
# # pressed=st.button("click me")
# # print(pressed)

# from profile import markdown_code

# st.title("My GenAi frontend journey")
# st.header("I specialize pre training")
# st.subheader("happy to get started")
# image_url = "https://i.imgur.com/7TMeNCS.png"
# st.image(image_url, caption="MP Profile picture", use_container_width=False)
# uploaded_image = st.file_uploader("Upload your profile picture", type=["png", "jpg", "jpeg"])
# if uploaded_image:
#     st.image(uploaded_image, caption="Uploaded image", use_container_width=False)
# st.markdown(markdown_code)


# creating form
import streamlit as st
import time

st.write("Gen AI Form")

with st.form("my_key"):            # with is used in context; only when the user click on submit that streamlit runs not as you change each character; context manager
    
   
   
    username = st.text_input(label="Please enter username")
    email = st.text_input(label="Please enter email")
    prompt = st.text_area(label="Input chars to be made meaning of", key="three")
    submit = st.form_submit_button(label="Submit Characters(chars)")
    
    
 
    # validating the form
    if not username or not  email or not prompt:
        st.error("Please fill in all fields")
    # if not username:
    #     st.error("Please fill in all fields")
    # elif not  email:
    #      st.error("Please fill in all fields")
    # elif not  prompt:
    #      st.error("Please fill in all fields")
    else:
        st.balloons()
        
        # showing validation message
        st.success("Validating...")

        st.subheader("Validated Information")
        user= st.write(f"{username}")
        user= st.write(f"{email}")
        user= st.write(f"{prompt}")  
        
        # Simulate progress bar
        progress = st.progress(0)
        for i in range(100):
                  time.sleep(0.02)  # simulate computation
                  progress.progress(i +1)
                  
        st.success("✔ Genaration Complete")
        
        

import streamlit as st
# using/creating sidebars
st.sidebar.title("Settings")
temperature = st.sidebar.slider("Creativity", 0.0, 1.0, 0.7)
model_choice= st.sidebar.selectbox("Model", ["GPT-4", "Gemini", "Claude", "OpenAI", "Perplexity", "Grok", "Copilot", "Midjourney", "Apple Intelligence"])

# creating tabs
# separating content into multiple pages without navigating
st.subheader("Tabs")
tab1, tab2 = st.tabs(["✍ Prompt", "📑 Output" ])
with tab1:
    st.text_area("Enter your prompt", key="two")
with tab2:
    st.write("Generated results appear here")
    
# creating columns
# placing elements side by side(for example; inputs on the left and results on the right)
st.subheader("Columns")
col1, col2 = st.columns(2)
with col1:
    st.text_input("Enter prompt")
with col2:
    st.write("AI results go here")
    
# creating containers
# group of related elemets and allor for dynamic updates inside the group
st.subheader("Container")
container= st.container()

container.write("Generated Text Area")
btn = container.button("Generate Text")

# Expander
# Hide/Show details on demand --useful for advanced settings or explanations
st.subheader("Expander")
with st.expander("Advanced Options"):
    st.slider("Max Tokens", 100, 1000)
    st.checkbox("Stream Output")
    
# Empty (st.empty)
# Reserve a space for content that updates later (for example; dynamic result areas)
st.subheader("Empty")
placeholder= st.empty()

if st.button("Generate"):
    placeholder.write("🔄 Generating...")
    # simulate generation
    placeholder.write("✔ Done! Here's the result.")
    
# combine layouts for GenAI App
st.title("🧠 GenAI Prompt Generator")
# Sidebar settings
st.sidebar.title("Settings")
temp = st.sidebar.slider("Creativity (temperature)", 0.0, 1.0, 0.7)
# Tabs
tab3, tab4 = st.tabs(["📑 Prompt", "📃 Output"])
with tab3:
    prompt1 = st.text_area("Enter your prompt", key="one")
with tab4:
    st.write("**AI Output:**")
    
if st.button("Generate", key="button3"):
        st.success(f"Responses from model (temp-{temp}) for: {prompt1}")