# Open AI Memory Chat Bot

This is a LangChain project that requires specific installation requirements and a virtual environment to run. Below are the instructions to set up the project on your local machine.

## Cloning the Repository

1. Clone the project repository by running the following command:

```
git clone https://github.com/vovann2003/Open-AI-Memory-Bot.git
```

2. Navigate to the project directory:

```
cd <repository>
```

## Prerequisites

Before proceeding, please make sure you have the following:

- Python 3.7 or higher installed on your system
- pip package installer for Python

## Virtual Environment Setup

1. Create a new virtual environment by running the following command:

```
python3 -m venv venv
```

2. Activate the virtual environment:

```
source venv/bin/activate (macOS/Linux)
venv\Scripts\activate (Windows)
```

## Installing Required Packages

1. Make sure your virtual environment is activated
2. Install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated

2. Run the LangChain application:

```
streamlit run run.py
```

3. Open your web browser and go to `http://localhost:80` to see the running application.

## Stopping the Application

To stop the application, press `Ctrl + C` in the terminal window where the server is running. Then deactivate the virtual environment:

```
deactivate
``` 

Congratulations, you have successfully installed and run the LangChain application!