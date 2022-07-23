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
    score = 'x'
  else:
    score = int(d[-1])
  
  new_entry[name] = score

print(new_entry)
