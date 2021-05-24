import datetime
import json
import os

from bs4 import BeautifulSoup

# Read the body of the last file
files = os.listdir('pages')
files.sort()

# Use consistent names, when there are multiple versions
clean_names = {
    'Maple Grove': 'Maple Grove Elementary',
    'Grant Ragan': 'Grant Ragan Elementary',
    'Waukee Innovation and Learning Center': 'Waukee ILC',
    'Priaireview School': 'Prairieview School'
}

def extract_data(fname):
    soup = BeautifulSoup(open(os.path.join('pages', fname), 'rb'), 'html5lib')
    table = soup.find('table')
    
    time = datetime.datetime.strptime(fname, 'page_%Y-%m-%d_%H-%M-%S.html')
    
    locations = []
    monitoring = None
    
    def read_locations(sect):
        for l in sect.find_all(['strong', 'p']):
            loc = l.string
            loc = clean_names.get(loc, loc)
            if loc:
                locations.append(loc)
                continue
            else:
                for ll in l.children:
                    loc = ll.string
                    if loc:
                        loc = loc.replace('\n', '')
                        loc = clean_names.get(loc, loc)
                        if len(loc):
                            locations.append(loc)
        
        # Newer cases fail
        if len(locations) == 0:
            for l in sect.children:
                loc = l.string
                if loc:
                    loc = loc.replace('\n', '')
                    loc = clean_names.get(loc, loc)
                    if len(loc):
                        locations.append(loc)
    
    for i, sect in enumerate(table.find_all('td')):
        if i == 0:
            students_string = sect.string.replace(' (in-person)', '')
            try:
                students = int(students_string)
                students_raw = None
            except ValueError:
                students = 2.5
                students_raw = students_string
        elif i == 2:
            try:
                staff = int(sect.string)
                staff_raw = None
            except ValueError:
                staff = 2.5
                staff_raw = sect.string
        elif i == 4:
            try:
                isolated = int(sect.string)
            except ValueError:
                isolated = 0
        elif time < datetime.datetime(2020, 10, 2, 20, 0, 0):
            if i == 6:
                read_locations(sect)
        else:
            if i == 6:
                try:
                    monitoring = int(sect.string)
                except ValueError:
                    pass
            elif i == 8:
                read_locations(sect)
    
    return time, students, staff, isolated, locations, students_raw, staff_raw, monitoring

def format_data(time, students, staff, isolated, students_raw = None, staff_raw = None, monitoring = None):
    out = {
            'time_utc': str(time),
            'positive_students': students,
            'positive_staff': staff,
            'number_isolated': isolated,
        }
    
    if students_raw:
        out['students_raw'] = students_raw
    
    if staff_raw:
        out['staff_raw'] = staff_raw
    
    if monitoring:
        out['monitoring'] = monitoring
    
    return out

# Used to keep track of cases
data = []
prev_data = None
curr_locs = {}

# Used to keep track of buildings
data_buildings = []
build_start = {}
build_end = {}

# Add one data point from before I started tracking
data.append(format_data("2020-09-03 03:12:20", 2, 3, 97))

for f in files:
    time, students, staff, isolated, locations, students_raw, staff_raw, monitoring = extract_data(f)
    curr_data = (students, staff, isolated, monitoring)
    
    if curr_data != prev_data:
        new_data = format_data(time, students, staff, isolated, students_raw=students_raw, staff_raw=staff_raw, monitoring=monitoring)
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
