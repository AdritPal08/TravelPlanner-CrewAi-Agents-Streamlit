from crewai import Agent
from textwrap import dedent
# from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import OpenAI
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
# from tools.browser_tools import BrowserTool
import streamlit as st
import re

GROQ_API = st.secrets["GROQ_API_KEY"]
# GROQ_API = os.getenv("GROQ_API_KEY")
class TravelAgents:
    def __init__(self):
        #OpenAI
        # self.OpenAIGPT35 = ChatOpenAI(
        #     model_name="gpt-3.5-turbo", temperature=0.7)
        # self.llm_1 = ChatGroq(
        #     api_key=os.getenv("GROQ_API_KEY_1"),
        #     model="llama-3.1-70b-versatile"
        # )
        # self.llm_2 = ChatGroq(
        #     api_key=os.getenv("GROQ_API_KEY_2"),
        #     model="llama-3.1-70b-versatile"
        # )
        # self.llm_3 = ChatGroq(
        #     api_key=os.getenv("GROQ_API_KEY_3"),
        #     model="llama-3.1-70b-versatile"
        # )
        # self.llm_4 = ChatGroq(
        #     api_key=os.getenv("GROQ_API_KEY_4"),
        #     model="llama-3.1-70b-versatile"
        # )
        # self.llm_5 = ChatGroq(
        #     api_key=os.getenv("GROQ_API_KEY_5"),
        #     model="llama-3.1-70b-versatile"
        # )
        # self.llm_6 = ChatGroq(
        #     api_key=os.getenv("GROQ_API_KEY_6"),
        #     model="llama-3.1-70b-versatile"
        # )
        # self.llm_7 = ChatGroq(
        #     api_key=os.getenv("GROQ_API_KEY_7"),
        #     model="llama-3.1-70b-versatile"
        # )
        self.llm = ChatGroq(
            api_key=GROQ_API,
            model="llama-3.1-70b-versatile"
        )
        # self.llm = ChatGoogleGenerativeAI(model="gemini-pro",verbose = True,temperature = 0.1)

        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        
        #Gemini
        # self.GeminiPro = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
        # self.GeminiAdvanced = ChatGoogleGenerativeAI(model="gemini-advanced", temperature=0.7)
        # self.GeminiAdvanced=ChatGoogleGenerativeAI(model="gemini-pro",
        #                    verbose=True,
        #                    temperature=0.5,
        #                    google_api_key=os.getenv("GOOGLE_API_KEY"))

    def Trip_Planner_Agent (self): #1
        return Agent(
            role="The lead agent responsible for coordinating the entire trip planning process.",
            backstory=dedent(
                f"""An experienced travel consultant with a passion for creating unforgettable journeys tailored to each client's preferences. 
                I have decades of expereince."""),
            goal=dedent(f"""
                        Develop a detailed, personalized travel itinerary that covers all aspects of the trip, including transportation, famous local cuisine, dining options, accommodation, weather, daily activities, budget, and local experiences.
                        Gather user requirements, delegate tasks to specialized agents to gather information, and assemble a comprehensive trip plan document.
                        """),
            # tools=[
            #     SearchTools.search_internet,
            #     CalculatorTools.calculate
            # ],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=self.llm,
        )

    def Destination_Research_Agent(self): #2
        return Agent(
            role="An expert on gathering information in depth  about destinations, attractions, and local experiences based on the user's preferences and travel dates.",
            backstory=dedent(
                f"""A well-traveled explorer with a wealth of knowledge about different cultures, customs, and attractions worldwide."""),
            goal=dedent(
                f"""Analyze and recommend the most suitable destination for the user's trip including famous places, local cuisine, and cultural experiences, considering factors like weather, events, costs, and alignment with their interests."""),
            tools=[SearchTools.search_internet,
                #    BrowserTool.scrape_and_summarize_website
                   ],
            allow_delegation=True,
            verbose=True,
            memory=True,
            llm=self.llm,
        )

    def Accommodation_Agent(self): #3
        return Agent(
            role="An expert in finding suitable accommodation options based on user preferences and budget.",
            backstory=dedent(f"""A seasoned traveler with a keen eye for comfort, amenities, and value for money."""),
            goal=dedent(
                f"""To provide a curated list of accommodation options with detailed information and current pricing."""),
            tools=[
                SearchTools.search_internet,
                # BrowserTool.scrape_and_summarize_website,
                CalculatorTools.calculate
            ],
            verbose=True,
            allow_delegation=True,
            memory=True,
            llm=self.llm,
        )
    
    def Transportation_Agent(self): #4
        return Agent(
            role="An expert in planning efficient and cost-effective transportation for the trip.",
            backstory=dedent(f"""A well-versed traveler with extensive knowledge of various transportation modes and logistics."""),
            goal=dedent(
                f"""To provide a detailed transportation plan, including modes of travel, schedules, and pricing."""),
            tools=[
                SearchTools.search_internet,
                # BrowserTool.scrape_and_summarize_website,
                CalculatorTools.calculate
            ],
            verbose=True,
            allow_delegation=True,
            memory=True,
            llm=self.llm,
        )
    
    def Weather_Agent(self): #5
        return Agent(
            role="An expert in providing accurate weather forecasts and advisories for the trip dates.",
            backstory=dedent(f"""A meteorologist with a deep understanding of weather patterns and their impact on travel plans."""),
            goal=dedent(
                f"""To provide detailed weather information for the trip dates, including forecasts and advisories."""),
            tools=[SearchTools.search_internet,
                #    BrowserTool.scrape_and_summarize_website
                   ],
            verbose=True,
            allow_delegation=True,
            memory=True,
            llm=self.llm,
        )
        
    def Itinerary_Planner_Agent(self): #6
        return Agent(
            role="An expert in creating well-structured and engaging daily itineraries for the trip for the chosen destination, including activities, dining, and accommodation options.",
            backstory=dedent(f"""A meticulous travel planner with a keen eye for detail and a knack for creating well-paced, immersive experiences."""),
            goal=dedent(
                f"""To create a detailed daily itinerary that balances must-see attractions with unique local experiences, ensuring a well-rounded and enjoyable trip based on the user's preferences, interests, and the outputs from other agents."""),
            tools=[SearchTools.search_internet,
                #    BrowserTool.scrape_and_summarize_website
                   ],
            verbose=True,
            allow_delegation=True,
            memory=True,
            llm=self.llm,
        )
    
    def Budget_Analyst_Agent(self): #7
        return Agent(
            role="Analyze and provide cost estimates for various aspects of the trip, including Transportation , accommodations, activities, and food(meals, etc..).",
            backstory=dedent(f"""A financial expert with a deep understanding of travel costs and a talent for finding the best deals and optimizing budgets."""),
            goal=dedent(
                f"""Provide a comprehensive budget breakdown for the trip, ensuring transparency and helping the user make informed decisions."""),
            tools=[
                SearchTools.search_internet,
                # BrowserTool.scrape_and_summarize_website,
                CalculatorTools.calculate
            ],
            verbose=True,
            allow_delegation=True,
            memory=True,
            llm=self.llm,
        )