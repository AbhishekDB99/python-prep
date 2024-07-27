# Update sheet1 to duplicate the outer values for inner values using sheet3 as the reference
for index, row in sheet3.iterrows():
    length_usl = row['Length USL']
    length_lsl = row['Length LSL']
    cap_usl = row['Cap USL']
    cap_lsl = row['Cap LSL']
    tensile_usl = row['Tensile USL']
    tensile_lsl = row['Tensile LSL']
    
    # Update LENGTH
    sheet1.loc[sheet1['Test'] == 'LENGTH - Outer', ['USL', 'LSL']] = [length_usl, length_lsl]
    sheet1.loc[sheet1['Test'] == 'LENGTH - Inner', ['USL', 'LSL']] = [length_usl, length_lsl]
    
    # Update CAP VALUE
    sheet1.loc[sheet1['Test'] == 'CAP VALUE - Outer', ['USL', 'LSL']] = [cap_usl, cap_lsl]
    sheet1.loc[sheet1['Test'] == 'CAP VALUE - Inner', ['USL', 'LSL']] = [cap_usl, cap_lsl]
    
    # Update WELD TENSILE
    sheet1.loc[sheet1['Test'] == 'WELD TENSILE - Right', ['USL', 'LSL']] = [tensile_usl, tensile_lsl]
    sheet1.loc[sheet1['Test'] == 'WELD TENSILE - Left', ['USL', 'LSL']] = [tensile_usl, tensile_lsl]

# Save the updated sheet1 to a new Excel file
new_file_path = '/mnt/data/infinityqs_final.xlsx'
with pd.ExcelWriter(new_file_path, engine='xlsxwriter') as writer:
    sheet1.to_excel(writer, sheet_name='Sheet1', index=False)
    sheet3.to_excel(writer, sheet_name='Sheet3', index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Final Updated Sheet 1", dataframe=sheet1)

new_file_path
