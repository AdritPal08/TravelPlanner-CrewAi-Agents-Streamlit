import streamlit as st
from streamlit_lottie import st_lottie
import datetime
from main import TripCrew
import os
import cv2
from PIL import Image
import cv2
import numpy as np
import random
import sys
from AgentProcess_Streamlit import StreamToExpander
import textwrap



today = datetime.datetime.now().date()
next_year = today.year + 1
next_month = today.month + 1
next_day = today.day
next_daterange = datetime.date(next_year, next_month, next_day)

def to_markdown(text):
    # Remove the indentation from the text
    text = textwrap.dedent(text)
    # Add the markdown syntax manually
    # text = "\n" + text.replace("•", "*")
    text = text.replace("•", " ")
    text = text.replace("*", " ")
    # text = text.replace("-", " ")
    # Return the markdown-formatted string
    return text

def get_random_image(folder_path, width, height):
    """Gets a random image from a specified folder and resizes it."""
    images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    random_image_path = os.path.join(folder_path, random.choice(images))

    img = cv2.imread(random_image_path)
    resized_img = cv2.resize(img, (width, height))
    rgb_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    return rgb_img


folder_path = 'Cover Images'
new_width, new_height = 1584, 396 
random_image = get_random_image(folder_path, new_width, new_height)


# Define the main app function
st.set_page_config(page_title="Trip Planner Agent", page_icon="🏖️", layout="centered", initial_sidebar_state = "auto")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Display a header
st.header("✈️ 🎫 :red[Trip Planner] :green[Agent] 🏝️ 🗺️",divider= 'rainbow')
# Display some text
st.write("Let AI agents plan your next vacation! 🏖️")


with st.sidebar:
    st_lottie("https://lottie.host/e1de7a95-db4b-4844-b7af-04ccc2eabb4f/fsFmquVkPw.json")
    st.header("Enter your trip details 👇")
    with st.form("my_form"):
        origin = st.text_input("📍 From where will you be traveling from?",placeholder="Kolkata, West Bengal, India")
        destination = st.text_input("🏝️ Which location you are interested in visiting?",placeholder="Bali, Indonesia")
        date_range = st.date_input(
                "📅 Date range you are interested in traveling?",
                min_value=today,
                value=(today, today + datetime.timedelta(days=6)),
                format="MM/DD/YYYY",
            )
        interests = st.text_area("🍹🛍️ High level interests and hobbies or extra details about your trip?",
                                     placeholder="2 adults who love swimming, dancing, hiking, and eating")

        person = st.number_input("👩‍👩‍👧‍👦 No of person travelling?", min_value=1, step=1, format="%d", placeholder = 2)
        
        submitted = st.form_submit_button("💫 Submit")
    
    st.divider()
    
    st.sidebar.markdown(
        """
        🚀 Created by : [**Adrit**](https://www.linkedin.com/in/adritpal/)
        """,
            unsafe_allow_html=True
        )
    st.sidebar.info("Click the logo to visit GitHub repo", icon="👇")
    st.sidebar.markdown(
            """
        <a href="https://github.com/AdritPal08/TravelPlanner-CrewAi-Agents-Streamlit" target="_blank">
            <img src="https://raw.githubusercontent.com/joaomdmoura/crewAI/main/docs/crewai_logo.png" alt="CrewAI Logo" style="width:100px;"/>
        </a>
        """,
            unsafe_allow_html=True
        )
    
if submitted:
    if origin and origin.strip() and destination and destination.strip() and date_range and interests and interests.strip() and person != "":
        start_date, end_date = date_range
        formatted_start_date = start_date.strftime("%dth %B, %Y")
        formatted_end_date = end_date.strftime("%dth %B, %Y")
        og_date_range = f"{formatted_start_date} - {formatted_end_date}"
        with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
            with st.container(height=500, border=False):
                sys.stdout = StreamToExpander(st)
                trip_crew = TripCrew(origin, destination, og_date_range, interests, person)
                result = trip_crew.run()
                
            status.update(label="✅ Trip Plan Ready!",
                      state="complete", expanded=False)
        
        st.subheader("Here is your Trip Plan", anchor=False, divider="rainbow")
        # st.image("travel_1.png")
        st.image(random_image, channels='RGB')
        st.markdown(result)
        output_str = str(result)
        output_bytes = output_str.encode('utf-8')
        st.download_button(
                    label="Download the Trip Plan",
                    data=to_markdown(output_bytes.decode('utf-8')),
                    file_name="Trip Plan.txt",
                    mime="text/plain",)
             

    else :
        st.warning("Please fill out all fields before submitting.")
