# Rydah-Task
REST APIs for google oauth

# API Documentation

Welcome to the API documentation! 
This document provides information on how to access and explore the API endpoints

## Tech Stack

Utilizes the following technologies and frameworks:

- Python: A powerful programming language used for the backend development.
- Django REST framework: A powerful and flexible toolkit for building Web APIs.
- Git: A distributed version control system used for tracking changes in source code during software development.

## Prerequisite Download
1. Python
2. Vscode
3. PostgreSQL

## How to Run the Project

To run the project on your local machine, follow these steps:

### Check my GoogleOauth.md file for instructions on how to use googleoauth


## Cloning the Repository

To access the source code and documentation, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Check this https://testdriven.io/blog/django-rest-auth/ on how to create your Google developer console to access GOOGLE_CLIENT_SECRET for your .env file
4. Use the following command to clone the repository:

   ```bash
   git clone https://github.com/Jayteemighty/Rydah-Task.git

## Running the Server

Before accessing the API documentation, ensure that you have the necessary dependencies installed and the server running. Follow these steps:

1. Navigate to the root directory of the cloned repository.
2. Install the required dependencies using the following command:

   ```bash
   pipenv install

3. Make sure to setup your environment variable(.env) check the .env.example
4. Start the server by running the following command:

   ```bash
   python manage.py runserver

## Accessing API Documentation

1. To access the API documentation using Swagger, follow these steps:

2. Open your web browser. Enter the following URL in the address bar:

   ```bash
   http://localhost:8000/schema/
   
This URL points to the Swagger UI interface for the API documentation.

3. Press Enter to navigate to the Swagger interface.

4. Explore the API endpoints such as:
   ```bash
   /api/register - Register a new user
   /api/login - Logs in an existing user
   /accounts/google/signup - verify new users
   

## Conclusion

The API documentation provides comprehensive information on the available endpoints and how to interact with them. If you have any questions or issues, feel free to reach out through tolujosh1@gmail.com.

Thank you for using our API!

## NOTE: Open to corrections. Please feel free to make any necessary changes.




