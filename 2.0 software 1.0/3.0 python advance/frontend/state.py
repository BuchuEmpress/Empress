import streamlit as st
import time
# count = 0                  # evry time state changes, it reruns the application so the state chaanges and it increments and when you click on the button the again,
# the application reruns and state is zero before in increments to 1
# if st.button("Increment"):
#     count += 1       
    
# .............................................................

# if "count" not in st.session_state:
#     st.session_state.count=0
    
# if st.button("Increment"):
#     st.session_state.count += 1                
# st.write(f"Count: {st.session_state.count}")

# if "step" not in st.session_state:
#     st.session_state.step = 1
# if "info" not in st.session_state:
#     st.session_state.info = {}

# def next_page(name, email, more_info):
#      st.session_state.step = 2
#      st.session_state.info["name"] = name
#      st.session_state.info["email"] = email
#      st.session_state.info["more_info"] = more_info
     
# def prev_page():
#     st.session_state.step = 1
    
    
# if st.session_state.step == 1:
#     st.header("Please enter your info")
#     st.write("Trying to be nice")
#     name = st.text_input("Enter your username", value=st.session_state.info.get("name", ""))      # the 'value.....' 
#     email = st.text_input("Enter your email", value=st.session_state.info.get("email", ""))
#     more_info = st.text_area("Tell us more about yourself", value=st.session_state.info.get("more_info", ""))
    
#     next = st.button("Next Page",                                     # typing it in form ("next page",on_click=next_page(name, emal, more_info)) is just calling the function instaed of passing it as a callback
#                      on_click=next_page,
#                      args=(name, email, more_info))                #reruns the application to update then at the second click shows info that why it's clicks twice
#     # here callbacks(ia basically a function that gets called automatically when somethin happens) comie in
#     # if next:
#         # st.session_state.step = 2
#         # st.session_state.info["name"] = name
#         # st.session_state.info["email"] = email
#         # st.session_state.info["more_info"] = more_info
        
# elif st.session_state.step == 2:
#     st.header("📑Confirm your information")
#     st.subheader(f"📄Your information is:")
#     st.write(f"Name: {st.session_state.info["name"]}")
#     st.write(f"Email: {st.session_state.info["email"]}")
#     st.write(f"More about you: {st.session_state.info["more_info"]}")
    
#     check_box = st.checkbox("Confirm your info")
#     if check_box:
#         st.balloons()
     
       
#     st. button("Prev", on_click=prev_page)
#         # if prev:
#             # st.session_state.step = 1

# ................................................................................................... 
            

# def display_info():
#     if name  not in st.session_state:
#             return f"{name}: Has no information recored"
#                   # get the average score
#     else:
#         return {                                        # return all details for that student in a dictionary form
#             "Name": name,
#             "Email": email,
#             "More about you": more_info,
#         }
   
# st.write(return)

# ...........................................................................................


# without callbacks
# simulating if an app has to process each word for 2 seconds(like 100 lines of code for an AI would be a nightmare)
# the advantage of using callbacks is because it doesn;t rerun the application every time a word is typed using the callbacks; it just calls/is passed and runs at once
# def expensive_search(query):
#     time.sleep(2)   # simulate heavy work
#     return f"Results for '{query}'"
# query = st.text_input("Search for something")
# if query:
#     st.write(expensive_search(query))
    
    
    
def expensive_search():
    query = st.session_state.query
    time.sleep(2)   # simulate heavy work
    st.session_state.results =  f"Results for '{query}'"
    
st.text_input("Search for something", key="query")
st.button("Run Search", on_click=expensive_search)

if "results" in st.session_state:
    st.write(st.session_state.results)
    
    
