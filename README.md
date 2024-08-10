# Travel Planner Crew AI Agents - Streamlit App 🏝️🗺️

Travel Planner Agents are dedicated to crafting personalized and comprehensive travel itineraries tailored to your specific needs. By considering your travel origin, destination, interests, date range, and the number of travelers, our agents curate the perfect travel plan, ensuring an engaging and memorable experience.

This project demonstrates how autonomous AI agents can collaborate and execute complex tasks efficiently, with a user-friendly Streamlit interface.


## It leverages the following technologies:

`Crew AI:` Crew AI is an open-source framework that allows engineers to orchestrate multiple autonomous AI agents to work together on complex tasks. It provides a way to break down larger problems into smaller subtasks and assign each subtask to a specialized AI agent. These agents can then collaborate and share information to solve the overall problem more effectively.

`Python:` Python is a popular, versatile programming language known for its simplicity and readability. It is widely used for various applications, including web development, data analysis, machine learning, and automation tasks. Python's extensive ecosystem of libraries and frameworks makes it a powerful tool for developers.

`LLaMA 3.1 (70b):` LLaMA (Lean Large-Language Model) is a family of large language models developed by Meta AI. The 3.1 (70b) version refers to a specific model variant with 70 billion parameters. Large language models like LLaMA are trained on vast amounts of text data, allowing them to understand and generate human-like text for various natural language processing tasks.

`Groq API:` Groq API provides access to Groq's powerful AI inference platform. It enables developers to leverage their advanced hardware and software for rapid and efficient AI model execution.

`Streamlit:` Streamlit is an open-source Python library that simplifies the process of building interactive data visualization and machine learning web applications. It allows developers to create user interfaces by writing Python scripts, making it easier to share data-driven applications with others.


## Project Structure
The project consists of the following files and directories:

**agents.py:**  Defines Crew AI agents responsible for specific tasks in the travel itinerary planning process, such as gathering user preferences, searching for relevant destinations and activities, and curating the final itinerary.

**tasks.py:**  Defines Crew AI tasks for each agent involved in the travel itinerary planning process, such as collecting user input, fetching travel data from various sources, and generating the itinerary.

**search_tools.py:**  Provides custom search tools using APIs (e.g., SERPER) to gather relevant information for travel planning, such as destinations, attractions, accommodations, and transportation options.

**file_io.py:**  Contains functions for saving the generated travel itinerary in markdown format.

**main.py:**  The main script that instantiates Crew AI agents, tasks, and the language model (e.g., LLaMA 3.1 (70b)). It then forms a Crew object and kicks off the travel itinerary planning process.

**app.py:** Defines and creates the Streamlit application, providing a user-friendly interface for users to input their travel preferences and receive personalized itineraries.

**.env (hidden file):**  Stores API keys (e.g., SERPER API key, Groq API KEY) used by the project.

**requirements.txt:**  Stores all the python libraries. 


## How it Works

1. **Destination Research:** The `Destination_Research_Agent` analyzes and recommends the most suitable destination for the user's trip, considering factors like famous places, local cuisine, cultural experiences, weather, events, costs, and alignment with their interests.

2. **Accommodation Curation:** The `Accommodation_Agent` provides a curated list of accommodation options with detailed information and current pricing.

3. **Transportation Planning:** The `Transportation_Agent` provides a detailed transportation plan, including modes of travel, schedules, and pricing.

4. **Weather Analysis:** The `Weather_Agent` provides detailed weather information for the trip dates, including forecasts and advisories.

5. **Itinerary Planning:** The `Itinerary_Planner_Agent` creates a detailed daily itinerary that balances must-see attractions with unique local experiences, ensuring a well-rounded and enjoyable trip based on the user's preferences, interests, and the outputs from other agents.

6. **Budget Analysis:** The `Budget_Analyst_Agent` provides a comprehensive budget breakdown for the trip, ensuring transparency and helping the user make informed decisions.

7. **Trip Planning Orchestration:** The `Trip_Planner_Agent` develops a detailed, personalized travel itinerary that covers all aspects of the trip, including transportation, famous local cuisine, dining options, accommodation, weather, daily activities, budget, and local experiences. It gathers user requirements, delegates tasks to specialized agents to gather information, and assembles a comprehensive trip plan document.


## Running the Project
1. **Fork or Clone the Repository::** 

Fork or clone this repository to your local machine using Git.

2. **Install Requirements:**

Install the necessary libraries.

```bash
pip install -r requirements.txt

```

3. **Set Up Environment Variables:**

Create a `.env` file in your project directory and add any required API keys (e.g., SERPER API key, Groq API KEY).

4. **Run the main file:**

```bash
python main.py
```
4. **Run the streamlit application file:**

```bash
streamlit run app.py
```
This will initiate the Crew AI workflow and generate a perfect trip plan for you in Markdown and text formats.


## Conclusion

The Travel Planner Agents project showcases the power of autonomous AI agents for personalized travel planning. By leveraging user-provided details (origin, destination, interests, date range, number of travelers), these agents collaboratively create comprehensive itineraries, ensuring an engaging and memorable travel experience.

This project not only facilitates a user-friendly Streamlit interface for effortless interaction but also demonstrates the capabilities of AI in efficient task execution. The collaboration between multiple agents highlights the potential for complex problem-solving through AI cooperation.


## License :

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [GNU General Public License v3.0](https://github.com/AdritPal08/AI-News-Letter-Generator-with-Crew-AI-Python-and-ChatGPT/blob/main/LICENSE)


## Follow Me :

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adritpal/)


## Authors

- [@Adrit Pal](https://github.com/AdritPal08)


## 
- If you like my work and it helped you in anyway then please do ⭐ the repository it will motivate me to make more amazing projects