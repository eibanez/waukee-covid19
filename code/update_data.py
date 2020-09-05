import os

from bs4 import BeautifulSoup

# Read the body of the last file
files = os.listdir('pages')
files.sort()

def extract_data(fname):
    soup = BeautifulSoup(open(fname, 'r'), 'html.parser')
    table = soup.find('table')
    
    locations = []
    
    for i, sect in enumerate(table.find_all('td')):
        if i == 0:
            students = int(sect.string)
        elif i == 2:
            staff = int(sect.string)
        elif i == 4:
            isolated = int(sect.string)
        elif i == 6:
            locations = [l for l in sect.find_all('strong')]
    
    print(fname)
    print(students, staff, isolated, locations)

for f in files:
    extract_data(os.path.join('pages', f))
