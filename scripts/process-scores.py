import json

NAMES = ['Jessica', 'Brian', 'Eduardo']

with open('master-scores.json') as f:
    data = json.load(f)

scores = []

for d in data:
    # Skip days before Brian started playing
    if d['wordle_no'] < 244:
        continue
    
    # Calculate minimum score
    win_score = min(d[n] for n in NAMES if d[n] != 'X')
    winners = {n: True for n in NAMES if d[n] == win_score}
    
    for n in NAMES:
        new_score = dict(wordle_no = d['wordle_no'], name = n, score = d[n], win=0, win_alone=0)
        
        if winners.get(n):
            new_score['win'] = 1
            if len(winners) == 1:
                new_score['win_alone'] = 1
        
        scores.append(new_score)

with open('score-by-player.json', 'w') as f2:
    json.dump(scores, f2, indent = 2)
