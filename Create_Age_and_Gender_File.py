# This code creates a file to validate test case of ChatGPT with proper antidepressant completions for age and gender
import openpyxl
import pandas as pd


def generate_validation_file(pivot_sheet):
    
    # constants
    pivot_start_row = 6
    pivot_strata_column = 'B'
    pivot_completion_column = 'U'
    
    # initialize dictionary for data frame conversion
    data_dict = dict()    
    data_dict['age_low'] = []
    data_dict['age_high'] = []
    data_dict['gender'] = []
    data_dict['antidepressant'] = []
    # loop through workbook pivot sheet and fill dictionary
    for row in range(pivot_start_row, pivot_sheet.max_row+1):
        strata_cell = "{}{}".format(pivot_strata_column, row)
        strata = pivot_sheet[strata_cell].value
        
        if strata is None:
            continue
        
        # parse strata with attributes split using '|'        
        strata_segments = strata.split('|')
        
        # process only strata with age and gender
        if len(strata_segments) != 2: 
            continue
        elif 'age:' not in strata.lower() and 'gender:' not in strata.lower():
            continue
            
        
        # loop into strata segments
        for segment in strata_segments:
            # age
            if 'age:' in segment.lower():
                age_range = segment.split(':')[1].strip()
                age_low = age_range.split('-')[0].strip()
                age_high = age_range.split('-')[1].strip()
            
            # gender
            elif 'gender:' in segment.lower():
                gender = segment.split(':')[1].strip().lower()
        
        completion_cell = "{}{}".format(pivot_completion_column, row)
        completion = pivot_sheet[completion_cell].value
        
        data_dict['age_low'].append(int(age_low))
        data_dict['age_high'].append(int(age_high))
        data_dict['gender'].append(gender)
        data_dict['antidepressant'].append(completion)
    
    
    data_df = pd.DataFrame(data_dict)
    
    return data_df

def main():

    # define constants
    workbook_file_path = 'C:/Users/vladc/OneDrive/Documents/GMU Research/AI Chat for Depression/Reference Files/Subgroups and Optimal Antidepressants.xlsx'
    pivot_sheet_name = 'Prompts and Completions'

    
    workbook = openpyxl.load_workbook(workbook_file_path)
    pivot_sheet = workbook[pivot_sheet_name]
    
    # get relevant data
    data_df = generate_validation_file(pivot_sheet)

    # write data to a file    
    csv_file_path = 'C:/Users/vladc/OneDrive/Documents/GMU Research/AI Chat for Depression/Reference Files/test_validation_file.csv'    
    data_df.to_csv(csv_file_path)
    
    
    return

if __name__ == "__main__":
    main()