# arionkoder-efficient-data-pipeline
This repository contains the implementation for the 'Memory-Efficient Data Pipeline' exercise.


# Usage Options
1) Fully Containerized Application
    Simply run the command `sudo docker-compose up` in a terminal;

    Wait for both services to start: the RabbitMQ container and the FastAPI application.


2) Running Applications Locally
    Create and activate a Python virtual environment using the appropriate command for your OS (Linux or Windows);

    Install Poetry with `pip install poetry`, then navigate to the `app` directory and run `poetry install`;

    Inside the `app` folder, start the FastAPI application with: `uvicorn main:app --reload`

    To run RabbitMQ separately, use the following command:`sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management`
    This will start a standalone RabbitMQ container.


# Testing the Application
As this application acts as a webhook, it must be triggered by an external script.
We recommend using the sample provided in `script_test.py`. However, any method that can make HTTP requests is acceptable.

# Inspecting the Database
You can access the API documentation at: http://localhost:8000/docs#/

Note: Due to the nature of the webhook, the POST endpoint cannot be tested directly through the documentation interface.
However, both GET (to retrieve saved data) and DELETE (to clear the database) endpoints can be used normally.

# Env Sample
The .env.sample file contains the environment variables required to run the application either locally (Local ENVs) or inside a container (Container ENVs).

The main difference between them is the RabbitMQ host address, which changes depending on whether the application is running in a fully containerized setup or not