import pandas as pd
import sys

excel_file_path = 'teste.xlsx'
identifier_columns = ['Var1', 'Var2']

xls = pd.ExcelFile(excel_file_path)

sheet_names = xls.sheet_names
patient_data = {}

for sheet_name in sheet_names:
    df = pd.read_excel(xls, sheet_name)
    for _, row in df.iterrows():
        patient_key = []
        for identifier in identifier_columns:
            patient_key.append(row[identifier])
        patient_key = tuple(patient_key)
        
        if patient_key not in patient_data:
            patient_data[patient_key] = {}
            
        for column in df.columns:
            if column not in identifier_columns:
                patient_data[patient_key][column] = row[column]

merged_df = pd.DataFrame.from_dict(patient_data, orient='index')
merged_df.reset_index(inplace=True)

for i in range(len(identifier_columns)):
    merged_df.rename(columns={f'level_{i}': identifier_columns[i]}, inplace=True)

merged_df.to_excel('merged_data.xlsx', index=False)