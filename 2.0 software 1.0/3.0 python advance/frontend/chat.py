import streamlit as st
st.set_page_config(layout="wide")
st.title("💭 Chat with DEEPSEED")
with st.container():
    st.info("👨‍🦰 welcome to the world of deeseeds")
    st.write("👱‍♀️ 🌱 Based on your message, I can provide some insights on this. 💡 ")   
with st.sidebar:
    st.columns(2) 
st.markdown(
    """
    <div style="
    border: 2px solid #000;
    border-radius: 10px;
    min-height: 400px;
    border-color: grey;
    padding: 15px;
    margin: auto;">
    <style>
    .info-box {
        border-radius: 8px;
        background-color: grey;
        background-color: rgba(112, 112, 116, 0.5);
        margin-left: 250px;
        min-height: 60px;
    }
    .joy {
        font-size: 34px;
        padding: 10px;
    }
    .girl {
        font-size: 60px;
    }
    </style>
    
    <div class="info-box"><p style="font-size:25px padding: 20px;"><span class="joy">👨‍🦰 </span>
    welcome to the world of deepseeds</p></div>
    <p style="font-size:25px padding: 20px;"><span class="girl">👱‍♀️</span> 🌱 Based on your message, I can provide some insights on this. 💡</p>
    """, 
    
 unsafe_allow_html=True
)
st.markdown("------")
with st.form(key="key_one"):
    st.write("Message DEEPSEED:")
    
    st.markdown("""
                <style>
                .div.stFormSubmitButton > button {
                    width: 100%;
                }
                </style>
                """, unsafe_allow_html=True)
    col1, col2 = st.columns([4,1])
    with col1:
     prompt = st.text_input("",placeholder="Type your message here")
    with col2:
     submit = st.form_submit_button("Send 🚀", use_container_width=True)
st.write("💭 2 messages in this conversation◽Session: bc9c1729....") 
# **********************************************************************
# side bar content
st.sidebar.title("🌱 DEEPSEED")
st.sidebar.markdown("<div class='italic'>one seed at a time</div>", unsafe_allow_html=True)
# italize using the font style
st.markdown("""
                <style>
                .italic {
                font-style: italic;
                color: grey
                    }""", unsafe_allow_html=True)
st.sidebar.markdown("------")
# ---------------------------------------------------------------------
st.sidebar.header("📊 Session Stats")
# make sidebar large enough to accomodate two colums
st.markdown(
    """
    <style>
    [data-testid="stSidebar"]{
        width: 350px ! important;
        min-width: 350px ! important;
    }
    
    </style>
    """, unsafe_allow_html=True
)
# aligning columns to appear side by side
with st.sidebar:
 col1, col2 = st.columns(2)
 with col1:
    st.write("Messages")
    st.markdown("<div class='two'>2</div>", unsafe_allow_html=True)
 with col2:
    st.write("Total")
    st.markdown("<div class='two'>2</div>", unsafe_allow_html=True)
    st.markdown("""
                <style>
                .two{
                    font-size: 40px;
                }
                </style>
                """, unsafe_allow_html=True)   
st.sidebar.markdown("------")
# -----------------------------------------------------------------------------
st.sidebar.header("🚀 Quick Actions")
with st.sidebar:
    
    st.button("💡 Tell me a joke", use_container_width=True)
    st.button("💡 Explain AI", use_container_width=True)
    st.button("💡 Help brainstorm", use_container_width=True)
    st.button("💡 Writing tips", use_container_width=True)
    st.button("💡 Book recommendations", use_container_width=True)
    st.sidebar.markdown("------")
# --------------------------------------------------------------
with st.sidebar:
 st.markdown("### ⚙ Controls", unsafe_allow_html=True)
# #  st.markdown("""c
#             <div style="display: flex; align-items: center; font-size: 18px;">
#             ❄⚙
#             <span style="margin-left: 8px;"><b>Controls</b></span>
#             .con {
#                 color:white;
#             }
#             </style>
#             """, unsafe_allow_html=True)
