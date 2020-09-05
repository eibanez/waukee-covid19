import datetime
import os
import json

from bs4 import BeautifulSoup

# Read the body of the last file
files = os.listdir('pages')
files.sort()

def extract_data(fname):
    soup = BeautifulSoup(open(os.path.join('pages', fname), 'rb'), 'html5lib')
    table = soup.find('table')
    
    time = datetime.datetime.strptime(fname, 'page_%Y-%m-%d_%H-%M-%S.html')
    
    locations = []
    
    for i, sect in enumerate(table.find_all('td')):
        if i == 0:
            students = int(sect.string)
        elif i == 2:
            staff = int(sect.string)
        elif i == 4:
            isolated = int(sect.string)
        elif i == 6:
            for l in sect.find_all('strong'):
                loc = l.string
                if loc:
                    locations.append(loc)
                    continue
                else:
                    for ll in l.children:
                        loc = ll.string
                        if loc:
                            loc = loc.replace('\n', '')
                            if len(loc):
                                locations.append(loc)
    
    return time, students, staff, isolated, locations

data = []
prev_data = None
curr_locs = {}

data_buildings = []
build_start = {}
build_end = {}

for f in files:
    time, students, staff, isolated, locations = extract_data(f)
    curr_data = (students, staff, isolated)
    
    if curr_data != prev_data:
        new_data = {
            'time_utc': str(time),
            'positive_students': students,
            'positive_staff': staff,
            'number_isolated': isolated,
        }
        data.append(new_data)
        prev_data = curr_data
    
    for l in locations:
        try:
            build_start[l]
        except KeyError:
            build_start[l] = str(time)
        build_end[l] = str(time)
    
    curr_buildings = {b: True for b in locations}
    
    all_builds = [k for k, _ in build_start.items()]
    for b in all_builds:
        if curr_buildings.get(b):
            continue
        
        new_build = {
            'location': b,
            'start_utc': build_start[b], 
            'end_utc': build_end[b], 
        }
        data_buildings.append(new_build)
        build_start.pop(b)
        build_end.pop(b)

# Add any remaining dates
for k, v in build_start.items():
    new_build = {
        'location': k,
        'start_utc': build_start[k],
        'end_utc': build_end[k], 
    }
    data_buildings.append(new_build)

with open(os.path.join('docs', 'data.json'), 'w') as f:
    f.write(json.dumps(data, indent=2))

with open(os.path.join('docs', 'buildings.json'), 'w') as f:
    f.write(json.dumps(data_buildings, indent=2))
