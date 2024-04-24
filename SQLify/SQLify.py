from dotenv import load_dotenv
load_dotenv() 
import os
import streamlit as st
import psycopg2  

import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql):

    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"), 
        user=os.getenv("DB_USER"), 
        password=os.getenv("DB_PASSWORD"), 
        host=os.getenv("DB_HOST"), 
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def clean_sql_query(sql_query):
   
    return sql_query.replace('```sql', '').replace('```', '').strip()


prompt = ["""
    You are an AI expert in converting English questions into SQL queries!
    The SQL database is structured with the following tables and their key columns:
    
    1. airports (airport_code, name, city, country, latitude, longitude)
    2. aircrafts (aircraft_code, model, capacity)
    3. flights (flight_id, flight_no, departure_airport, arrival_airport, departure_time, arrival_time, aircraft_code)
    4. passengers (passenger_id, first_name, last_name, email)
    5. bookings (booking_id, booking_date, passenger_id)
    6. tickets (ticket_id, booking_id, flight_id, seat, class, price, status)
    
    For example,
    Question: How many flights depart from JFK Airport?
    SQL Answer: SELECT COUNT(*) FROM flights WHERE departure_airport = 'JFK';
    
    Question: What are the details of passengers booked on flight FL100?
    SQL Answer: SELECT p.first_name, p.last_name, p.email FROM passengers p JOIN bookings b ON p.passenger_id = b.passenger_id JOIN tickets t ON b.booking_id = t.booking_id WHERE t.flight_id = (SELECT flight_id FROM flights WHERE flight_no = 'FL100');
    
    Ensure that your SQL queries do not include the word 'sql' explicitly in the output and avoid using backticks (`) around table or column names. SQL queries should be clear, concise, and correctly formatted to reflect the structure of the database.
    """
]


# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")


if submit:
    raw_sql_query = get_gemini_response(question, prompt)
    sql_query = clean_sql_query(raw_sql_query)  
    st.write(f"Generated SQL Query: {sql_query}")  
    try:
        response = read_sql_query(sql_query)
        st.subheader("The Response is:")
        for row in response:
            st.write(row)
    except Exception as e:
        st.error(f"Failed to execute SQL query: {str(e)}")
