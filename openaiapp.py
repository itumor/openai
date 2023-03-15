import os
import openai
openai.organization =  os.getenv("OPENAI_API_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")
modellist = openai.Model.list()
print(modellist)
