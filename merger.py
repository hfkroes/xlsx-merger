import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
identifier_columns = sys.argv[3:]

xls = pd.ExcelFile(input_file)

sheet_names = xls.sheet_names
line_data = {}

for sheet_name in sheet_names:
    df = pd.read_excel(xls, sheet_name)
    for _, row in df.iterrows():
        line_key = []
        for identifier in identifier_columns:
            line_key.append(row[identifier])
        line_key = tuple(line_key)
        
        if line_key not in line_data:
            line_data[line_key] = {}
            
        for column in df.columns:
            if column not in identifier_columns:
                line_data[line_key][column] = row[column]

merged_df = pd.DataFrame.from_dict(line_data, orient='index')
merged_df.reset_index(inplace=True)

for i in range(len(identifier_columns)):
    merged_df.rename(columns={f'level_{i}': identifier_columns[i]}, inplace=True)

merged_df.to_excel(output_file, index=False)