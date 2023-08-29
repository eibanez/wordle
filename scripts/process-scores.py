import json
import os

NAMES = ['Jessica', 'Brian', 'Eduardo']

with open('master-scores.json') as f:
    data = json.load(f)

scores = []
master_out = []
streak_tracker = {n: 1 for n in NAMES}

for d in sorted(data, key=lambda item: item.get('wordle_no')):
    # Skip days before Brian started playing
    if d['wordle_no'] < 244:
        continue
    
    # Copy for the master output file
    master_out.append(d)
    
    # Calculate minimum score
    win_score = min(v for k, v in d.items() if v != 'X')
    winners = {k: True for k, v in d.items() if v == win_score}
    
    for n in NAMES:
        # New row to be added
        try:
            new_score = dict(wordle_no = d['wordle_no'], name = n, score = d[n])
        except KeyError:
            streak_tracker[n] += 1
            continue
        
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

with open(os.path.join('docs', 'master-scores.json'), 'w') as f2:
    json.dump(master_out, f2, indent = 2)
