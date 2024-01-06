import openai
import os
import PyPDF2

openai.api_key = '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'

model = 'text-davinci-003'

initial_system_prompt = """ 
You are a chatbot that summarizes research documents so that patients with depression can understand alternative treatments for their depression.
"""

message_start = [
    {
        "role": "system",
        "content": initial_system_prompt,
    },
]

documents = []
path = "./research_documents"
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(path, filename)
        document_text = ""
        print(pdf_path)
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page1 = reader.pages[0]
            document_text += page1.extract_text()
            documents.append(document_text)

for document in documents:
    dataset = []
    dataset.append('Document:')
    dataset.append(document)
    dataset.append('User:')
    dataset.append("Please summarize the findings and conclusions of the study.")

    document_prompt = '\n'.join(dataset)

    prompt = f"{message_start}\n{document_prompt}"

    response = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        model=model,
        )

    print("Response:\n", response.choices[0].text.strip())