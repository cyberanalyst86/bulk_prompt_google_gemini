import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import pandas as pd

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


df = pd.DataFrame()

# Used to securely store your API key
from google.colab import userdata
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro-latest')

query_list = []
response_list = []

df_input = pd.read_excel("input.xlsx")

input_list = df_input["input"].to_list()

for input in input_list:

  print(input)

  print("--------------------------------------------------------------------\n")

  query = "help me to do a SWOT analysis of  " + str(input)

  print(query)

  print("--------------------------------------------------------------------\n")

  query_list.append(query)

  response = model.generate_content(query)

  print(response.text)

  response_list.append(response.text)

df["company"] = system_list
df["query"] = query_list
df["response"] = response_list

df.to_excel("output.xlsx", index=False)


