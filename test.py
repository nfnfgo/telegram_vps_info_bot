# You can use this file to delete LineBreak in config.py

with open('config.py','r') as f:
    text=f.read()

text=text.replace('\n','')

with open('config.py','w') as f:
    f.write(text)