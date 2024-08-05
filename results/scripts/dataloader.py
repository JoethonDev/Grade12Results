# import pandas as pd
import openpyxl
import os
from results.models import grades
import time
from .bot_sender import send_registered
import sys

def run():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Replace 'your_excel_file.xlsx' with the actual name of your Excel file
    excel_file_name = 'results_1.xlsx'

    # Construct the full path to the Excel file
    excel_file_path = os.path.join(current_directory, excel_file_name)
    try:
        # Read the Excel file into a DataFrame
        start_time = time.time()
        df = openpyxl.load_workbook(excel_file_path)
        sheet = df.active
        print(f"Read File Time : {time.time() - start_time}")
        num = 1
        records = []
        header = [cell.value.strip() for cell in sheet[1]]
        start_time = time.time()
        for row in sheet.iter_rows(min_row=2, values_only=True):
            values = dict(zip(header, row))
            # Filter the DataFrame based on the "seating_no" column
            name = values['arabic_name']
            degree = values['total_degree']
            state = values['student_case_desc']
            seatNo = values['seating_no']
            records.append(
                grades(name=name, totalDegree=degree, state=state, seat_no=seatNo)
            )
            if num % 10000 == 0:
                print(f'result #{num}')
            num += 1
        print(f"Creating records Time : {time.time() - start_time}")
        start_time = time.time()
        grades.objects.bulk_create(records)
        print(f"Inserting records Time : {time.time() - start_time}")
        start_time = time.time()
        send_registered()
        print(f"Sending Results records Time : {time.time() - start_time}")
        print('done')

    except Exception as e:
        print(f"Error: {e}")

