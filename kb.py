import urllib.request
from transformers import pipeline


qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
def kb_qa(question, context):
    answer = qa_pipeline(question=question, context=context)
    return answer["answer"]

#source from raw github repo
url = 'https://raw.githubusercontent.com/kalyan-raparthi/kitsw-chatbot/refs/heads/main/data.txt'
res = urllib.request.urlopen(url) 
context = res.read().decode("utf8")
#print(context)

while True:
    query = input(">>> ")
    if query == "exit":
        break
    answer = kb_qa(query, context)
    print(answer)
