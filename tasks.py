from crewai import Task
from textwrap import dedent

class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def Final_Trip_Plan(self, agent, context, origin, destination,travel_dates, interests, person, callback_function):  # Trip_Planner_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Assemble the final trip plan and create details documentation. 
            **Description**: 
            - The Trip Planner Agent acts as the project manager, combining outputs from specialized coworker agents into a cohesive trip itinerary document.
            - This document will be presented in a user-friendly, paragraph-based format.
            - Generated document will be in the markdown format.
            
 
            **Parameters**: 
            - Traveling From : {origin}
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Traveler Interests: {interests}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            context=context,
            callback=callback_function,
            expected_output = 
            """
            {
  "Trip Summary": "Details and interesting overview of the trip.",
  
  "Travel Highlights": [
    {"Name": "Highlight 1", "Description": "Brief description"},
    // ... more highlights ...
  ],
  
  "Transportation": [
    "Getting There": A list of all transportation options from Traveling From Place to Travel Destination
    [
    {
        "Mode": "Transportation mode",
        "Travel Time" : "Total travel time",
        "Departure": "Departure time", 
        "Arrival": "Arrival time", 
        "Cost": "Price Range", 
        "Details": "Details"
    },
    ... more Transportation mode and option(Flight, Train, Bus, or others) ..,
    "Best Option": "Details comparison between all the available transportation modes of their travel timing and their cost, Then recommended a good option."
    ],
    "Getting Around": A list of dictionaries of all the local transportation options with details.
    [
      {"Mode": "Transportation mode", "Details": "Details", "Price":"Price Range"},
      ... more Transportation mode
    ],
    "Passes": A list of available passes with details information.
    [
      {"Name": "Pass name", "Cost": "Price", "Benefits": "Benefits", "Eligibility": "Eligibility"},
      ... more Passes Information
    ]
  ],
  "Accommodations": A curated list of accommodation options with detailed.
  [
    {
      "Name": "Accommodation name",
      "Address": "Address",
      "Contact": "Contact information",
      "Type": "Accommodation type",
      "Price range": "Price range",
      "Amenities": ["Amenity 1", "Amenity 2"],
      "Accessibility": "Accessibility features",
      "Sustainability": "Certifications",
      "Reviews": "Rating and reviews",
      "Booking": "Booking link or contact"
    },
    // ... more accommodations option...
  ],
  
  "Daily Itinerary": Detailed day-by-day itinerary for the trip.
  [
    {
      "Date": "YYYY-MM-DD",
      "Plan": "Detail Planning of the day."
      "Activities": ["Activity 1", "Activity 2"],
      "Transportation": ["Mode 1", "Mode 2"],
      "Dining": ["Dining option 1", "Dining option 2"],
      "Weather" : "Weather forcast of the day",
      "Packing suggestions" : "Packing suggestions of the day."
      
    },
    // ... more days ...
  ],
  
  "Local Cuisine": A list of all local cuisine with details. 
  [
    {"Cuisine": "Cuisine name", "Restaurants": [{"Name": "Restaurant name ", "Price": "Price range"}]},
    // ... more cuisines ...
  ],
  
  "Weather": Detailed information about the daily weather forcast for the trip.
  {
    "Daily": [
      {"Date": "YYYY-MM-DD", "Forecast": "Summary"}
    ],
    "Hourly": [
      {"Time": "HH:MM", "Forecast": "Summary"}
    ],
    "Alerts": ["Alert 1", "Alert 2"],
    "Realtime": "Current conditions",
    "Historical": "Historical data"
  },
  
  "Budget": A detailed breakdown of the estimated budget plan for the trip with proper calculation.
  {
    "Breakdown": {
      "Category1": "Amount",
      "Category2": "Amount"
    },
    "Total": "Total amount"
  },
  
  "Cost Saving": A detailed list of cost saving recommendations and suggestions.
  ["Recommendation 1", "Recommendation 2"],
  
  "Additional Tips": General travel advice and any additional recommendations.
  ["Tip 1", "Tip 2"]
}

            """,
        )
    
    def Research_Destination_Highlights(self, agent, origin, destination,travel_dates, interests, person):  # Destination_Research_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Research destination attractions and experiences. 
            **Description**: Gather in-depth information about the destination's top attractions, historical sites, and local customs, special events, daily activity recommendations local experiences based on user interests. 
            considering factors like: User interests, Travel dates, Sustainability, Accessibility, Budget Friendly, Family-friendliness,  Unique experiences. 

            **Parameters**: 
            - Traveling From : {origin}
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Traveler Interests: {interests}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A detailed list of recommended attractions ,experiences, local customs, special events, daily activity recommendations, hidden gems, cultural hotspots, must-visit landmarks with descriptions, images, and practical information (e.g., opening hours, ticket prices, location). ",
        )
        
    def Discover_Local_Cuisine(self, agent, destination,travel_dates, person):  # Destination_Research_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Research local cuisine and dining options. 
            **Description**: Investigate the destination's culinary scene, famous dishes, and recommended dining establishments with prices.
            
            **Parameters**: 
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A list of local cuisine recommendations and dining options with prices.",
        )
    
    def Find_Your_Perfect_Stay(self, agent, destination,travel_dates, person):  # Accommodation_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Search for accommodation options. 
            **Description**: Explore hotels, vacation rentals, or other accommodation types based on location, Number of travellers, Tavel date, Amenities, Accessibility, Sustainability ratings, Guest reviews and ratings. 

            **Parameters**: 
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = dedent("""A curated list of accommodation options with detailed information, 
            including : 
            •	Name, address, and contact information
            •	Type of accommodation
            •	Price range
            •	Amenities
            •	Accessibility features
            •	Sustainability certifications
            •	Guest reviews and ratings
            •	Booking links or contact information
            """),
        )
    
    def Transportation_Between_Destinations(self, agent, origin, destination,travel_dates, person):  # Transportation_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Plan transportation between destinations. 
            **Description**: Explore transportation options (flights, trains, buses, etc.) for traveling between the origin and destination, 
            Consider factors such as: Departure and arrival times, Cost (budget-friendly), Travel time, Comfort and convenience, Sustainability, Accessibility.

            **Parameters**: 
            - Origin : {origin}
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A comparison of transportation options, including details on transportation mode, departure/arrival times, costs, travel duration, and sustainability ratings.",
        )
    
    def Plan_Local_Transportation(self, agent, destination,travel_dates, person):  # Transportation_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Plan local transportation. 
            **Description**: Investigate local transportation options (public transit, taxis, rental cars, etc.) for getting around the destination.
            
            **Parameters**: 
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A list of local transportation recommendations with details.",
        )
    
    def Info_Transportation_Passes (self, agent, destination,travel_dates, person):  # Transportation_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Provide information on transportation passes or tickets. 
            **Description**: Research and recommend transportation passes or tickets that can save money and time for the user. 
            Consider options such as:
                            •	City passes: Combined transportation and attraction tickets.
                            •	Public transportation passes: Daily, weekly, or monthly passes for buses, trains, and subways.
                            •	Airport transfers: Shared or private transportation options.
                            •	Car rental deals: Discounts, insurance packages, and additional driver fees.
                            
                            
            **Parameters**: 
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A list of available transportation passes or tickets, including their costs, benefits, and eligibility criteria.",
        )

    def Weather_Forecasts (self, agent, destination,travel_dates):  # Weather_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Retrieve weather forecasts. 
            **Description**: Gather comprehensive weather information for the destination during the specified travel dates. 
            Include:
                            •	Daily forecasts: Temperature, precipitation, wind speed, and humidity for each day.
                            •	Hourly forecasts: Detailed weather conditions for specific times of the day.
                            •	Weather alerts: Warnings for severe weather conditions (storms, hurricanes, etc.).
                            •	Real-time updates: Current weather conditions and forecasts.
                            •	Historical data: Average weather patterns for the destination.
                            

            **Parameters**: 
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A detailed weather report for trip duration, including daily and hourly forecasts, weather alerts, real-time updates, and historical data. The report should be easily understandable and visually appealing.",
        )
        
    def Daily_Itineraries(self, agent, destination,travel_dates, interests, person):  # Itinerary_Planner_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Create daily itineraries. 
            **Description**: Develop a comprehensive and flexible day-by-day itinerary tailored based on the user's specific preferences, time constraints, and energy levels. 
            Incorporate:
                    •   Plan : Detail Planning of the day.
                    •	Activities : Detailed of all activities of the day.
                    •	Transportation: Efficient and cost-effective travel options.
                    •	Dining: Recommendations for local cuisine and dining experiences.
                    •	Accommodation: Relevant information about the lodging.
                    •	Weather: Considerations for outdoor activities and clothing.
                    •	Packing suggestions: Recommendations based on the itinerary and weather conditions (e.g., essential clothing, footwear, accessories).
                            

            **Parameters**: 
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Traveler Interests: {interests}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A detailed, personalized daily itinerary for the trip duration.",
        )
        
    def Budget_Plan (self, agent, destination,travel_dates, person):  # Budget_Analyst_Agent
        return Task(
            description=dedent(
                f"""
            **Task**: Create a budget plan. 
            **Description**: Analyze the costs of accommodations, transportation, activities, and food/dining options to create a detailed budget plan based on travel date range and number of travellers. Include:
                            •	Cost breakdowns: Itemized expenses for each category.
                            •	Total budget: Overall estimated cost of the trip.
                            •	Cost comparisons: Analyze different options within each category (e.g., compare hotel prices, transportation fares, activity costs).
                            •	Cost-saving recommendations: Suggest ways to reduce expenses without compromising the trip experience (e.g., choosing budget-friendly accommodations, opting for public transportation, exploring free activities).
                            •	Flexible budgeting: Offer options for different budget levels and priorities

            **Parameters**: 
            - Travel Destination: {destination}
            - Travel Date Range: {travel_dates}
            - Number of Person Travel :{person}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            async_execution=True,
            expected_output = "A comprehensive budget plan with detailed cost information, comparative analysis, and actionable cost-saving recommendations.",
        )