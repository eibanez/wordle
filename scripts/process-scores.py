import json
import os

NAMES = ['Jessica', 'Brian', 'Eduardo']

with open('master-scores.json') as f:
    data = json.load(f)

scores = []
streak_tracker = {n: 1 for n in NAMES}

for d in data:
    # Skip days before Brian started playing
    if d['wordle_no'] < 244:
        continue
    
    # Calculate minimum score
    win_score = min(d[n] for n in NAMES if d[n] != 'X')
    winners = {n: True for n in NAMES if d[n] == win_score}
    
    for n in NAMES:
        # New row to be added
        new_score = dict(wordle_no = d['wordle_no'], name = n, score = d[n], win=0, win_alone=0)
        
        # Mark whether it's a winning score
        if winners.get(n):
            new_score['win'] = 1
            if len(winners) == 1:
                new_score['win_alone'] = 1
        
        # Keep track of the current streak
        if d[n] == 'X':
            streak_tracker[n] += 1
        else:
            new_score['streak_id'] = streak_tracker[n]
        
        # Add score to overall array
        scores.append(new_score)

with open(os.path.join('docs', 'score-by-player.json'), 'w') as f2:
    json.dump(scores, f2, indent = 2)
