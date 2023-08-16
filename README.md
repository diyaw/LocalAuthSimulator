# LocalAuthSimulator
Explore the world of HTTP communication, authentication, and resource access through this Python-based simulation project. Simulate the interaction between a client, an Authorization Server, and a Resource API, gaining hands-on insights into the process of securing and retrieving data.

# HTTP Simulation Project

This is a Python project that simulates HTTP communication between a client, an Authorization Server, and a Resource API.

## Project Structure

README.md file:

# HTTP Simulation Project

## Project Structure

python_project/
├── authorization_server.py
├── resource_api.py
├── main.py
├── test_server_interactions.py
└── requirements.txt



## How to Set Up the Project

Follow these steps to set up and execute the project:

1. **Clone the GitHub Repository:**

   Clone the project repository from GitHub.

2. **Ensure You Have Python Interpreter or venv:**

   Make sure you have a Python interpreter installed, or create a virtual environment (venv) with Python.

3. **Install Required Packages:**

   Install the required packages by running the following command:

pip install -r requirements.txt


## How to Execute the Project

To execute the project, activate all three components one by one:

1. **Open Three Terminals:**

Open three separate terminal windows.

**Terminal 1:** Run the Authorization Server:

python authorization_server.py


**Terminal 2:** Run the Resource API:

python resource_api.py


**Terminal 3:** Run the Client Simulation:

python main.py


The output should resemble the following:

![Final Result](screenshots/final_result.png)

2. **Execute Unit Test Cases:**

After successful execution of the scripts, you can run the unit test cases using the following command:

python -m unittest test_server_interactions.py


In case you encounter errors related to ports already in use while executing scripts, you can kill the processes running on the ports 