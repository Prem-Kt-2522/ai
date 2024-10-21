import ollama

file = 'Astar.py'

with open(file, 'r') as data:
    content = data.read()

my_prompt = f'give output for this code {content}'

response = ollama.chat(model='llama3.2:1b',messages=[{'role': 'user','content': my_prompt}],stream=True)

for chunk in response:
  print(chunk['message']['content'], end='', flush=True)