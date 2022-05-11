import datetime
import json
import os

from bs4 import BeautifulSoup

# Read the body of the last file
files = [f for f in os.listdir('pages') if f.endswith('.html')]
files.sort()

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
                try:
                    cases = int(sect.string.replace(',', ''))
                except ValueError:
                    cases = 2.5
            except TypeError:
                if building == 'Total Students7':
                    building = 'Total Students'
                    cases = 7
                else:
                    cases_str = [s3 for s3 in [s2 for s2 in [s for s in sect.children][0].children][0].children][0]
                    try:
                        cases = int(cases_str.replace(',', ''))
                    except:
                        continue
            
            if building == 'Total':
                pass
            elif building == 'District Office':
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
                if time.startswith('2022-01-03'):
                    # Xmas break
                    new_data = {
                        'time': time.replace('2022-01-03', '2022-01-02'),
                        'type': building,
                        'cases': None
                    }
                    totals.append(new_data)
                
                # Override numbers that are way too high
                if (cases == 1210):
                    cases = 10
                
                new_data = {
                    'time': time,
                    'type': building,
                    'cases': cases
                }
                totals.append(new_data)
            else:
                try:
                    pd, t = start[building]
                    
                    if time.startswith('2022-01-03'):
                        # Xmas break
                        new_data = {
                            'start': t,
                            'end': prev_time,
                            'building': building,
                            'cases': pd
                        }
                        data.append(new_data)
                        
                        if cases > 0:
                            start[building] = (cases, time)
                        else:
                            start.pop(building)
                    elif pd != cases:
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
    
    prev_time = time

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
