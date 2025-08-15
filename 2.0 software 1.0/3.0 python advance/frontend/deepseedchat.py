import streamlit as st

st.set_page_config(layout="wide", page_title="DeepSeed Chatbot")


#initalizing the session state
if 'messages' not in st.session_state:
 st.session_state['messages'] = []

# function to send a fixed reply
def send_reply():
    return "🌱 Based on your message, I can provide some insights on this. 💡"

# Initialize a list to keep track of user messages only
if 'user_message_count' not in st.session_state:
    st.session_state['user_message_count'] = 0

st.title("💬 Chat with DEEPSEED")
# sidebar; not necessary
with st.sidebar:
    session_id = "bc9c1729"
    st.markdown(f"<div class=id>Session ID: {session_id}</div>", unsafe_allow_html=True)
    st.markdown("""
                <style>
                .id {
                    color: grey;
                    font-size: 19px;
                    font-style: italic
                }
                </style>
                """, unsafe_allow_html=True)
    # st.write(f"Total Messages: {st.session_state['user_message_count']}")


chat_log = st.empty()

st.markdown("---")

# form for sending messages
with st.form(key="message_form", clear_on_submit=True):
    col1, col2 = st.columns([3,1])
    with col1:
        user_message = st.text_input(label="Message DEEPSEED:", placeholder="Type your message here...")
    with col2:
        submit_button = st.form_submit_button("Send 🚀", use_container_width=True)


# Initialising variables if form is not submitted yey
if 'submit_button'not in locals():
    submit_button = False
if 'user_message' not in locals():
    user_message = ""


# process user message
if submit_button and user_message.strip() != "":
 #  increment message count
 st.session_state['user_message_count'] += 1
 
 # append user's message    
 st.session_state['messages'].append({'role': 'user', 'content': user_message})
 
 
 
 # Add bot's reply
 if st.session_state['user_message_count'] == 1:
      # determine when the bot replies
    # if this is user's first message, add a welcome message
     st.session_state['messages'].append({'role': 'bot', 'content':"📃 welcome to the world of deepseeds"})
 else:
    #  subsequently reply with fixed response
     reply = send_reply()
     st.session_state['messages'].append({'role': 'bot', 'content': reply})     #({'role':'bot', 'content': reply})
    
    

# display messages in a container

with chat_log.container(height=400, border=True):
    st.markdown("""
                <style>
                .stMarkdown {
                    margin-top: 0;
                    margin-bottom: 0;
                    padding-top: 0;
                    padding-bottom: 0;
                }
                </style>
                """, unsafe_allow_html=True)
    
    for msg in st.session_state['messages']:
        if not isinstance(msg, dict):
            st.write('Found a non-dict message:', msg)
            continue
        # st.write(msg['content'])
        # message_html = ""
        if msg['role'] == 'user':
            # user message on left
            html  = f"""
            <div style="text-align: left; margin: 2px 0;">
            <div style="display: inline-block; background-color:rgba(84, 118, 230, 0.2);
            padding: 60px; padding-right: 300px; border-radius: 10px; max-width: 800rem;
            height: 78px;">
            {msg['content']}
            </div>
            </div>
            """
            st.markdown(html, unsafe_allow_html=True)
        elif msg['role'] == 'bot':
            # bot message on right
            html = f"""
            <div style="text-align: right; margin: 2px 0;">
            <div style="display: inline-block; background-color:rgba(93, 191, 216, 0.2);
            color: white; padding: 60px; padding-left: 300px; border-radius: 10px; max-width: 800rem;
            height: 78px;">
            {msg['content']}
            </div>
            </div>
            """
            st.markdown(html, unsafe_allow_html=True)


st.write(f"💬 {len(st.session_state['messages'])} in this session◽Session {session_id}")   #counts to total messages


    
   
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
    st.markdown(f"<div class='two'>{st.session_state['user_message_count']}</div>", unsafe_allow_html=True)
 with col2:
    st.write("Total")
    st.markdown(f"<div class='two'>{st.session_state['user_message_count']}</div>", unsafe_allow_html=True)
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


# =============== Button Functionaity From Sidebar=========================
# initialize active nutton state
if 'active_button' not in st.session_state:
    st.session_state['active_button'] = None 
    
if 'show_container' not in st.session_state:
    st.session_state['show_container'] = False

# function to set active button
def set_active(button_name):
    st.session_state['active_button'] = button_name

def show_container():
    st.session_state['show_container'] = True

def hide_container():
    st.session_state['show_container'] = False
 

with st.sidebar:
    # using single session state variable that tracks which button is clicked
    if st.button("💡 Tell me a joke", use_container_width=True):
        show_container()
        set_active('joke')
    if st.button("💡 Explain AI", use_container_width=True):
        show_container()
        set_active('explain_ai')
    if st.button("💡 Help brainstorm", use_container_width=True):
        show_container()
        set_active('brainstorm')
    if st.button("💡 Writing tips", use_container_width=True):
        show_container()
        set_active('writing_tips')
    if st.button("💡 Book recommendations", use_container_width=True):
        show_container() 
        set_active('book_recommendations')
        
  
reply_title = ""
reply_text = ""      
# show fixed container if active button is set
if st.session_state["active_button"]:
    active = st.session_state['active_button']
    # determine the reply content
    if active == 'joke':
         st.session_state['reply_title'] = "Here's a joke for you!"
         st.session_state['reply_text'] = "Why did the seed go to the gym? To get sprouted!🤣🤣🤣🤣🤣"
    elif active == 'explain_ai':
         st.session_state['reply_title']  ="Explaining AI"
         st.session_state['reply_text'] = "Artificial Intelligence(AI) is the simulation of human intelligence in machines."
    elif active == 'brainstorm':
         st.session_state['reply_title'] = "Brainstorming Ideas"
         st.session_state['reply_text'] = "Let's generate some creative ideas together."
    elif active == 'writing_tips':
         st.session_state['reply_title'] = "Writing Tips"
         st.session_state['reply_text'] = "Always keep your audience in mind and be clear."
    elif active == 'book_recommendations':
         st.session_state['reply_title'] ="Book Recommendations"
         st.session_state['reply_text'] = "Here are some great books to read!"
    
       
       
# css for opacity transition
st.markdown ("""
<style>
#reply-container {
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
    background-color:rgba(93, 191, 216, 0.2); /*aqua semi transparent backkground*/
    padding: 20px;
    font-size: 30px;
    font-style: 'Baskerville Old Face';
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-top: 20px;
}
#reply-container.show {
    opacity: 1;
}
</style>
""", unsafe_allow_html=True)
         


container_html = ""
if st.session_state['show_container']:
    
 container_html = f"""
 <div id="reply-container" class="show">
  <h3>{st.session_state.get('reply_title', '')}</h3>
  <p>{st.session_state.get('reply_text', '')}</p>
   <form method="post">
   </form>
 </div> 
 """
st.markdown(container_html, unsafe_allow_html=True)

if st.button("Close Quick Action", key= "close_reply", on_click=hide_container(), use_container_width=True): 
    st.markdown(container_html, unsafe_allow_html=True)
else:
    pass   



st.sidebar.markdown("------")

# --------------------------------------------------------------
with st.sidebar:
 st.markdown("### ⚙ Controls", unsafe_allow_html=True)
# #  st.markdown("""

