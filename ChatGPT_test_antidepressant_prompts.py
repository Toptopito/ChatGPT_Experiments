import openai
import os
import pandas as pd

openai.api_key = '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'

model = "gpt-3.5-turbo-0613"

validation_file_path = "C:/Users/vladc/OneDrive/Documents/GMU Research/AI Chat for Depression/Reference Files/test_validation_file.csv"

validation_df = pd.read_csv(validation_file_path)

chat_input = ""
while(chat_input.lower() != 'exit'):
    chat_input = input("What is your age and gender (enter \"exit\" to end)? ")
    
    if chat_input.lower() == 'exit':
        break
    
    prompt = """Please look into the following data:\n {}. 
    Please also look at the following information provided by the user: {}.
    Categorize the age and gender of the user. 
    Then summarize the age group and gender of the user. 
    Then based on age and gender find the row in the data where the gender and age group match the information provided by the user.
    Then from that row tell the user the recommended antidepressant that matched the user's age group and gender.
    Do not tell the user about your process just your recommendation.
    
    Examples for finding the matching antidepressant:
    Example 1: "age": 39, "gender": male
    Result: "age_group": 20-40, "gender": male, "antidepressant": Venlafaxine | Desvenlafaxine

    Example 2: "age": 50, "gender": "female"
    Result: "age_group": 41-64, "gender": female, "antidepressant": Sertraline | Desvenlafaxine
    
    Example 3: "age": 87, "gender": "female"
    Result: "age_group": 80-89, "gender": female, "antidepressant": Desvenlafaxine
    
    I need you to output the antidepressant only. 
    For example, if the recommended antidepressant is Venlafaxine | Desvenlafaxine, just output Venlafaxine | Desvenlafaxine.
    If the recommended antidepressant is Desvenlafaxine, just output Desvenlafaxine.
    """.format(validation_df, chat_input)
    
    request = openai.ChatCompletion.create(
        model = model,
        messages = [
            {"role": "user", "content": prompt},
        ]
    )
    
    response = request['choices'][0]['message']['content']
    
    print("Response:", response)
