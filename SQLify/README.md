# SQLify : Gemini App To Retrieve SQL Data

This application uses Google's Generative AI to convert English questions into SQL queries, execute those queries against a PostgreSQL database, and display the results. It's designed to help users retrieve specific data from a database without needing to write SQL queries themselves.

## Features

- **Question to SQL Conversion**: Converts user-input questions into SQL queries using Google's Generative AI.
- **Database Query Execution**: Executes the generated SQL queries against a PostgreSQL database.
- **Result Display**: Displays the results of the SQL queries in a user-friendly format.

## Installation

1. Clone the repository.
2. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Google API Key and PostgreSQL database credentials in a `.env` file:
   
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=your_database_host
   DB_PORT=your_database_port
   ```

## Usage

1. Run the application:
   
   ```
   streamlit run app.py
   ```
3. Open the provided URL in your web browser.
4. Input a question related to the database content in the input field and click "Ask the question".
5. The application will generate an SQL query based on your question, execute it against the database, and display the results.

