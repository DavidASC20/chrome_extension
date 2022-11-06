# wolframalpha api id: AEYTEG-EQ5R5LXU2P

import wolframalpha

question = input('Question: ')
app_id = 'AEYTEG-EQ5R5LXU2P'
client = wolframalpha.Client(app_id)
res = client.query(question)
answer = next(res.results).text
print(answer)
