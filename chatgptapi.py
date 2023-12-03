import openai 

openai.api_key = open('api.txt','r').read().strip('\n')

completion = openai.ChatCompletion.creat()
