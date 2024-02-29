import pandas as pd
import streamlit as st

# SQL query templates
sql_templates = {
    'what flights are available from pittsburgh to baltimore on thursday morning': 'SELECT * FROM flights WHERE origin = "Pittsburgh" AND destination = "Baltimore" AND day = "Thursday" AND time = "morning"',
    'what is the arrival time in san francisco for the 755 am flight leaving washington': 'SELECT arrival_time FROM flights WHERE origin = "Washington" AND destination = "San Francisco" AND flight_number = "755" AND time = "morning"',
    'cheapest airfare from tacoma to orlando': 'SELECT MIN(airfare) FROM flights WHERE origin = "Tacoma" AND destination = "Orlando"',
    'round trip fares from pittsburgh to philadelphia under 1000 dollars': 'SELECT * FROM flights WHERE origin = "Pittsburgh" AND destination = "Philadelphia" AND round_trip_fare < 1000',
    'i need a flight tomorrow from columbus to minneapolis': 'SELECT * FROM flights WHERE origin = "Columbus" AND destination = "Minneapolis" AND day = "tomorrow"',
    'what kind of aircraft is used on a flight from cleveland to dallas': 'SELECT aircraft_type FROM flights WHERE origin = "Cleveland" AND destination = "Dallas"',
    'show me the flights from pittsburgh to los angeles on thursday': 'SELECT * FROM flights WHERE origin = "Pittsburgh" AND destination = "Los Angeles" AND day = "Thursday"',
    'all flights from boston to washington': 'SELECT * FROM flights WHERE origin = "Boston" AND destination = "Washington"',
    'what kind of ground transportation is available in denver': 'SELECT * FROM ground_transportation WHERE city = "Denver"',
    'show me the flights from dallas to san francisco': 'SELECT * FROM flights WHERE origin = "Dallas" AND destination = "San Francisco"',
    'show me the flights from san diego to newark by way of houston': 'SELECT * FROM flights WHERE origin = "San Diego" AND destination = "Newark" AND layover_city = "Houston"',
    'what is the cheapest flight from boston to bwi': 'SELECT * FROM flights WHERE origin = "Boston" AND destination = "BWI" ORDER BY airfare ASC LIMIT 1',
    'all flights to baltimore after 6 pm': 'SELECT * FROM flights WHERE destination = "Baltimore" AND time > "6 pm"'
}

# Streamlit app
def main():
    st.title('Flight Query Generator')

    # Text input for user to enter the query
    user_query = st.text_area('Enter your flight query:', height=100)

    # Button to execute the query
    if st.button('Generate SQL Query'):
        # Apply the conversion function to the user query
        sql_query = query_to_sql(user_query)

        # Display the SQL query
        st.subheader('Generated SQL Query:')
        st.code(sql_query, language='sql')

# Function to convert a query into an SQL query
def query_to_sql(query):
    for query_type, template in sql_templates.items():
        if query_type in query:
            return template
    return "SELECT * FROM airports WHERE city = 'Orlando'"

if __name__ == '__main__':
    main()
