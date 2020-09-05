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


with open(os.path.join('docs', 'data.json'), 'w') as f:
    f.write(json.dumps(data, indent=2))
