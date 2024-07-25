import pandas as pd
import os
from results.models import grades
import time
from .bot_sender import send_registered
import sys

def run():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Replace 'your_excel_file.xlsx' with the actual name of your Excel file
    excel_file_name = 'results.xlsx'

    # Construct the full path to the Excel file
    excel_file_path = os.path.join(current_directory, excel_file_name)
    try:
        # Read the Excel file into a DataFrame
        start_time = time.time()
        df = pd.read_excel(excel_file_path, usecols=['seating_no', 'arabic_name', 'total_degree', 'student_case_desc'], engine='openpyxl')
        print(f"Read File Time : {time.time() - start_time}")
        num = 1
        records = []
        start_time = time.time()
        for index, row in df.iterrows() :
        # Filter the DataFrame based on the "seating_no" column
            name = row['arabic_name']
            degree = row['total_degree']
            state = row['student_case_desc']
            seatNo = row['seating_no']
            records.append(
                grades(name=name, totalDegree=degree, state=state, seat_no=seatNo)
            )
            if num % 10000 == 0:
                print(f'result #{num}')
            num += 1
        print(f"Creating records Time : {time.time() - start_time}")
        start_time = time.time()
        grades.objects.bulk_create(records, batch_size=250000)
        print(f"Inserting records Time : {time.time() - start_time}")
        start_time = time.time()
        send_registered()
        print(f"Sening Results records Time : {time.time() - start_time}")
        print('done')

    except Exception as e:
        print(f"Error: {e}")

