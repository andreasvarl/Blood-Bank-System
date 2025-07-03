from database import conn, cursor
from Inventory import Inventory

class BloodBank:

    @staticmethod
    def donor_details(donor_name, donor_age, donor_blood_type):
        query = """
        INSERT INTO donor (donor_name, donor_age, donor_blood_type)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (donor_name, donor_age, donor_blood_type))
        conn.commit()

    @staticmethod
    def request_blood(hospital_name,
                      patient_name, patient_age, patient_blood_type,
                      donor_name, donor_age, donor_blood_type):
        query = """
        INSERT INTO request (
            hospital_name, patient_name, patient_age, patient_blood_type,
            donor_name, donor_age, donor_blood_type
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            hospital_name, patient_name, patient_age, patient_blood_type,
            donor_name, donor_age, donor_blood_type
        ))

        # Καταχώρηση αιμοδότη
        BloodBank.donor_details(donor_name, donor_age, donor_blood_type)

        # Ενημέρωση αποθέματος
        Inventory.add_blood(donor_blood_type)
        Inventory.deduct_blood(patient_blood_type)

        # Οριστικοποίηση αλλαγών
        conn.commit()