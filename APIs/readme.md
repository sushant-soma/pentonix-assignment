# Employee Management API

This Flask-based web application provides two APIs for managing employee data. It allows you to retrieve employee details by Employee Number (ENO) and also retrieve a list of employees by their department name (DNAME).

## Problem Description

The problem can be summarized as follows:

1. Create an in-memory database of employees and departments.
2. Implement an API to retrieve employee details by ENO.
3. Implement an API to retrieve a list of employees by DNAME.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x: You can download and install Python from the [official Python website](https://www.python.org/downloads/).
- Flask: This web application is built using Flask, a Python web framework. You can install Flask using pip:

    ```bash
    pip install Flask
    ```

## Solution Overview

The Flask application (`app.py`) is designed to address the problem described above. It includes two API endpoints:

1. **API for Retrieving Employee by ENO**:

    - Endpoint: `/api`
    - URL Example: `http://localhost:9000/api?ENO=1`
    - Description: This API retrieves employee details based on their Employee Number (ENO).
    - Exception Handling: The API handles invalid ENO format and returns appropriate error responses.

2. **API for Retrieving Employees by DNAME**:

    - Endpoint: `/api/employees_by_dname`
    - URL Example: `http://localhost:9000/api/employees_by_dname?DNAME=Admin`
    - Description: This API retrieves a list of employees based on their department name (DNAME).
    - Exception Handling: The API handles unexpected errors and returns appropriate error responses.

## Running the Application

Follow these steps to run the application:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/employee-management-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd employee-management-api
    ```

3. Install the required dependencies (Flask):

    ```bash
    pip install Flask
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

    This will start the application on port 9000 by default.

5. Access the APIs:

    - To retrieve employee details by ENO, use a URL like:
      `http://localhost:9000/api?ENO=1`

      ![image](https://github.com/sushant-soma/pentonix-assignment/assets/108216630/5c47218f-59e0-4a21-b081-af90db8f0167)


    - To retrieve a list of employees by DNAME, use a URL like:
      `http://localhost:9000/api/employees_by_dname?DNAME=Admin`

## API Usage

- When accessing the APIs, provide the required query parameters (`ENO` or `DNAME`) to retrieve the desired employee information.
- The APIs handle various scenarios, including valid and invalid inputs, and provide meaningful responses.
- Casting is type-safe, ensuring that inputs are correctly converted to their expected types.

## Troubleshooting

- If you encounter any issues, ensure that you have Python and Flask installed correctly.
- Double-check the URLs and query parameters when making requests to the APIs.

