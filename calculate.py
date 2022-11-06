# wolframalpha api id: AEYTEG-EQ5R5LXU2P

import wolframalpha

file = open('question.txt', 'r')  # the question will be saved to a text filed called 'question.txt'
question = file.readline()  # assuming question will saved to a single line

app_id = 'AEYTEG-EQ5R5LXU2P'
client = wolframalpha.Client(app_id)
res = client.query(question)
answer = next(res.results).text
print(answer)
