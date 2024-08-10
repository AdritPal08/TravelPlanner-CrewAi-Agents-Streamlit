import streamlit as st
import re


class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast(":robot_face: " + task_value)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary

            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "An expert on gathering information in depth  about destinations, attractions, and local experiences based on the user's preferences and travel dates." in cleaned_data: 
            # Apply different color 
            cleaned_data = cleaned_data.replace("An expert on gathering information in depth  about destinations, attractions, and local experiences based on the user's preferences and travel dates.", f":{self.colors[self.color_index]}[An expert on gathering information in depth  about destinations, attractions, and local experiences based on the user's preferences and travel dates.]")
            
        if "An expert in finding suitable accommodation options based on user preferences and budget." in cleaned_data:
            cleaned_data = cleaned_data.replace("An expert in finding suitable accommodation options based on user preferences and budget.", f":{self.colors[self.color_index]}[An expert in finding suitable accommodation options based on user preferences and budget.]")
        
        if "An expert in planning efficient and cost-effective transportation for the trip." in cleaned_data:
            cleaned_data = cleaned_data.replace("An expert in planning efficient and cost-effective transportation for the trip.", f":{self.colors[self.color_index]}[An expert in planning efficient and cost-effective transportation for the trip.]")
            
        if "An expert in providing accurate weather forecasts and advisories for the trip dates." in cleaned_data:
            cleaned_data = cleaned_data.replace("An expert in providing accurate weather forecasts and advisories for the trip dates.", f":{self.colors[self.color_index]}[An expert in providing accurate weather forecasts and advisories for the trip dates.]")
        
        if "An expert in creating well-structured and engaging daily itineraries for the trip for the chosen destination, including activities, dining, and accommodation options." in cleaned_data:
            cleaned_data = cleaned_data.replace("An expert in creating well-structured and engaging daily itineraries for the trip for the chosen destination, including activities, dining, and accommodation options.", f":{self.colors[self.color_index]}[An expert in creating well-structured and engaging daily itineraries for the trip for the chosen destination, including activities, dining, and accommodation options.]")
        
        if "Analyze and provide cost estimates for various aspects of the trip, including Transportation , accommodations, activities, and food(meals, etc..)." in cleaned_data:
            cleaned_data = cleaned_data.replace("Analyze and provide cost estimates for various aspects of the trip, including Transportation , accommodations, activities, and food(meals, etc..).", f":{self.colors[self.color_index]}[Analyze and provide cost estimates for various aspects of the trip, including Transportation , accommodations, activities, and food(meals, etc..).]")

        if "The lead agent responsible for coordinating the entire trip planning process." in cleaned_data:
            cleaned_data = cleaned_data.replace("The lead agent responsible for coordinating the entire trip planning process.", f":{self.colors[self.color_index]}[The lead agent responsible for coordinating the entire trip planning process.]")


        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []