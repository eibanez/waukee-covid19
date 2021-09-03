import datetime
import json
import os

from bs4 import BeautifulSoup

# Read the body of the last file
files = os.listdir('pages')
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

for fname in files[2:]:
    soup = BeautifulSoup(open(os.path.join('pages', fname), 'rb'), 'html5lib')
    table = soup.find('table')
    
    time = datetime.datetime.strptime(fname, 'page_%Y-%m-%d_%H-%M-%S.html')
    building = None
    cases = None
    
    for i, sect in enumerate(table.find_all('td')):
        # Skip the first entry of data
        if i <= 1:
            continue
        
        if building is None:
            building = sect.string
            continue
        else:
            try:
                cases = int(sect.string)
            except ValueError:
                cases = 2.5
            
            new_data = {
                'time': str(time),
                'building': building,
                'cases': cases
            }
            data.append(new_data)
            
            building = None
            cases = None

with open(os.path.join('docs', 'data2021.json'), 'w') as f:
    f.write(json.dumps(data, indent=2))
