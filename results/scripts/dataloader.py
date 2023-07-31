import pandas as pd
import os
from results.models import results

def run():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Replace 'your_excel_file.xlsx' with the actual name of your Excel file
    excel_file_name = 'results.xlsx'

    # Construct the full path to the Excel file
    excel_file_path = os.path.join(current_directory, excel_file_name)
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(excel_file_path, usecols=['seating_no', 'arabic_name', 'total_degree', 'student_case_desc'], engine='openpyxl')
        num = 1
        for index, row in df.iterrows() :
        # Filter the DataFrame based on the "seating_no" column
            name = row['arabic_name']
            degree = row['total_degree']
            state = row['student_case_desc']
            seatNo = row['seating_no']
            results.objects.create(name=name, totalDegree=degree, state=state, seat_no=seatNo)
            print(f'result #{num}')
            num += 1

        # If you want to retrieve only the "seating_no" column for the matching records:
        # records = filtered_df['seating_no'].tolist()
        print('done')
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
