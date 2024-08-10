from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from tools.file_io import save_markdown
import os
from dotenv import load_dotenv
load_dotenv()

class TripCrew:
    def __init__(self, origin, destination, date_range, interests, person):
        self.origin = origin
        self.destination = destination
        self.date_range = date_range
        self.interests = interests
        self.person = person
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents
        Trip_Planner_Agent = agents.Trip_Planner_Agent()
        Destination_Research_Agent = agents.Destination_Research_Agent()
        Accommodation_Agent = agents.Accommodation_Agent()
        Transportation_Agent = agents.Transportation_Agent()
        Weather_Agent = agents.Weather_Agent()
        Itinerary_Planner_Agent = agents.Itinerary_Planner_Agent()
        Budget_Analyst_Agent = agents.Budget_Analyst_Agent()

        # Custom tasks include agent name and variables as input
        Research_Destination_Highlights = tasks.Research_Destination_Highlights(
            Destination_Research_Agent, 
            self.origin, 
            self.destination,
            self.date_range, 
            self.interests, 
            self.person)

        Discover_Local_Cuisine = tasks.Discover_Local_Cuisine(
            Destination_Research_Agent, 
            self.destination,
            self.date_range, 
            self.person)

        Find_Your_Perfect_Stay = tasks.Find_Your_Perfect_Stay(
            Accommodation_Agent, 
            self.destination,
            self.date_range, 
            self.person)

        Transportation_Between_Destinations = tasks.Transportation_Between_Destinations(
            Transportation_Agent, 
            self.origin, 
            self.destination,
            self.date_range, 
            self.person)
        
        Plan_Local_Transportation = tasks.Plan_Local_Transportation(
            Transportation_Agent, 
            self.destination,
            self.date_range, 
            self.person)
        
        Info_Transportation_Passes = tasks.Info_Transportation_Passes (
            Transportation_Agent, 
            self.destination,
            self.date_range, 
            self.person)
        
        Weather_Forecasts = tasks.Weather_Forecasts (
            Weather_Agent, 
            self.destination,
            self.date_range)
        
        Daily_Itineraries = tasks.Daily_Itineraries(
            Itinerary_Planner_Agent, 
            self.destination,
            self.date_range, 
            self.interests, 
            self.person)
        
        Budget_Plan = tasks.Budget_Plan (
            Budget_Analyst_Agent, 
            self.destination,
            self.date_range, 
            self.person)
        
        Final_Trip_Plan = tasks.Final_Trip_Plan(
            Trip_Planner_Agent,
            [Research_Destination_Highlights, Discover_Local_Cuisine, Find_Your_Perfect_Stay, Transportation_Between_Destinations, Plan_Local_Transportation, Info_Transportation_Passes, Weather_Forecasts, Daily_Itineraries, Budget_Plan],  
            self.origin, 
            self.destination,
            self.date_range, 
            self.interests, 
            self.person,
            save_markdown)

        # Define your custom crew here
        crew = Crew(
            agents=[Destination_Research_Agent,
                    Accommodation_Agent,
                    Transportation_Agent,
                    Weather_Agent,
                    Itinerary_Planner_Agent,
                    Budget_Analyst_Agent,
                    Trip_Planner_Agent
                    ],
            tasks=[
                Research_Destination_Highlights,
                Discover_Local_Cuisine,
                Find_Your_Perfect_Stay,
                Transportation_Between_Destinations,
                Plan_Local_Transportation,
                Info_Transportation_Passes,
                Weather_Forecasts,
                Daily_Itineraries,
                Budget_Plan,
                Final_Trip_Plan
            ],
            process=Process.sequential,
            # manager_llm=ChatOpenAI( model=""),
            # memory= True,
            verbose=True,
            max_rpm= 5,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')
    # origin = input(
    #     dedent("""
    #   From where will you be traveling from?
    # """))
    origin = "Kolkata, West Bengal, India"
    # destination = input(
    #     dedent("""
    #   What are the cities options you are interested in visiting?
    # """))
    destination = "Thailand"
    # date_range = input(
    #     dedent("""
    #   What is the date range you are interested in traveling?
    # """))
    date_range = "25th August,2024 - 5th September,2024"
    # interests = input(
    #     dedent("""
    #   What are some of your high level interests and hobbies?
    # """))
    interests = "All the famous places."
    # person = input(
    #     dedent("""
    #   No of person travelling?
    # """))
    person = 3

    trip_crew = TripCrew(origin, destination, date_range, interests, person)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)  