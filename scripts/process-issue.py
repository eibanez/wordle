import json
import os

new_entry = {'wordle_no': int(os.environ['ISSUE_TITLE'])}

for d in os.environ['ISSUE_BODY'].upper().split():
  if d[0] == 'J':
    name = 'Jessica'
  elif d[0] == 'E':
    name = 'Eduardo'
  elif d[0] == 'B':
    name = 'Brian'
  else:
    raise RuntimeError('Invalid initial: {d[0]}')

  if d[-1] == 'X':
    score = 'X'
  else:
    score = int(d[-1])
  
  new_entry[name] = score

with open('master-scores.json', 'r') as f:
  data = json.load(f)

data.append(new_entry)

with open('master-scores.json', 'w') as f:
  json.dump(data, f, indent = 2)
