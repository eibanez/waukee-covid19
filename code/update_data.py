import datetime
import json
import os

from bs4 import BeautifulSoup

# Read the body of the last file
files = [f for f in os.listdir('pages') if f.endswith('.html')]
files.sort()

# Use consistent names, when there are multiple versions
#clean_names = {
#    'Maple Grove': 'Maple Grove Elementary',
#    'Grant Ragan': 'Grant Ragan Elementary',
#    'Waukee Innovation and Learning Center': 'Waukee ILC',
#    'Priaireview School': 'Prairieview School'
#}

# Used to keep track of cases
data = []
start = {}
totals = []
cumulative = []
prev_cumulative = None

for fname in files:
    soup = BeautifulSoup(open(os.path.join('pages', fname), 'rb'), 'html5lib')
    table = soup.find('table')
    
    time = str(datetime.datetime.strptime(fname, 'page_%Y-%m-%d_%H-%M-%S.html'))
    building = None
    cases = None
    
    for i, sect in enumerate(table.find_all('td')):
        # Skip the first entry of data
        if i <= 1:
            continue
        
        if building is None:
            if sect.string is None:
                for ch in sect.find_all('b'):
                    building = ch.string.strip()
            else:
                building = sect.string.strip()
            
            continue
        else:
            try:
                cases = int(sect.string)
            except ValueError:
                cases = 2.5
            
            if building == 'Total':
                pass
            elif building.startswith('Total Cumulative'):
                if cases != prev_cumulative:
                    new_data = {
                        'time': time,
                        'cases': cases
                    }
                    cumulative.append(new_data)
                    prev_cumulative = cases
            elif building.startswith('Total'):
                new_data = {
                    'time': time,
                    'type': building,
                    'cases': cases
                }
                totals.append(new_data)
            else:
                try:
                    pd, t = start[building]
                    
                    if pd != cases:
                        new_data = {
                            'start': t,
                            'end': time,
                            'building': building,
                            'cases': pd
                        }
                        data.append(new_data)
                        
                        if cases > 0:
                            start[building] = (cases, time)
                        else:
                            start.pop(building)
                except KeyError:
                    if cases > 0:
                        start[building] = (cases, time)
            
            building = None
            cases = None

for b, d in start.items():
    pd, t = d
    if pd > 0:
        new_data = {
            'start': t,
            'end': time,
            'building': b,
            'cases': pd
        }
        data.append(new_data)

with open(os.path.join('docs', 'data2021.json'), 'w') as f:
    f.write(json.dumps(data, indent=2))

with open(os.path.join('docs', 'totals2021.json'), 'w') as f:
    f.write(json.dumps(totals, indent=2))

with open(os.path.join('docs', 'cumulative2021.json'), 'w') as f:
    f.write(json.dumps(cumulative, indent=2))
