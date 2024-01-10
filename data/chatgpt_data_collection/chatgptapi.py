from openai import OpenAI

client = OpenAI(api_key=open('api.txt','r').read().strip('\n')) 
khabar = 'به گزارش عصرایران به نقل از فارس، علی شمخانی دبیر شورای عالی امنیت ملی گفت: به نظر می‌رسد دشمنان درصدد بودند حمله پهپادی انصار‌الله یمن به پالایشگاههای آرامکو را با حمله به تاسیسات عسلویه جبران کنند که ناکام ماندند.'

content = "از متن زیر 3 سوال همراه با جواب طرح کن. سوالات را در فرمت زیر قرار بده:سوال1:پاسخ1:سوال2:پاسخ2:سوال3:پاسخ3:{}".format(khabar)

completion = client.chat.completions.create(model = 'gpt-3.5-turbo-instruct',
messages = [{ "role":"user" , 'content':content}])

file = open("gpt_response.txt", "w") 
file.write(completion.choices[0].message.content)

file.close() 
