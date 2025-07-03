import psycopg2
import pandas as pd 

conn = psycopg2.connect(
    host="localhost",
    dbname="bloodbank",
    user="postgres",
    password="your_password"
)
cursor = conn.cursor()
print('The connection to the Database is Successful.')

def create_tables():
    
    donor_table = """
        CREATE TABLE IF NOT EXISTS donor (
        donor_id  SERIAL PRIMARY KEY,
        donor_name VARCHAR(30),
        donor_age INT,
        donor_blood_type VARCHAR(5)
        
    );
    """
    
    inventory_table = """
        CREATE TABLE IF NOT EXISTS inventory (
        blood_id  SERIAL PRIMARY KEY,
        blood_type VARCHAR(5),
        quantity INT
        
        
    );
    """
    
    request_table = """
        CREATE TABLE IF NOT EXISTS request (
        request_id  SERIAL PRIMARY KEY,
        hospital_name VARCHAR(30),
        patient_name VARCHAR(30),
        patient_age INT,
        patient_blood_type VARCHAR(5),
        donor_name VARCHAR(30),
        donor_age INT,
        donor_blood_type VARCHAR(5)
        
    );
    """
    
    cursor.execute(donor_table)
    cursor.execute(inventory_table)
    cursor.execute(request_table)
    conn.commit()
    print("Tables created successfully.")


    
print(__name__)
if __name__ == "__main__":
    create_tables()