import os

from bs4 import BeautifulSoup

# Read the body of the last file
files = os.listdir('pages')
files.sort()

def extract_data(fname):
    soup = BeautifulSoup(open(fname, 'r'), 'html.parser')
    print(soup.prettify())

for f in files[:1]:
    extract_data(f)
