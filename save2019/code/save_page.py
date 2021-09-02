import datetime
import os
import urllib.request

# Filename for the new file
ts = datetime.datetime.utcnow()
fname = str(ts).replace(':', '-').replace(' ', '_')[:19]
fname = os.path.join('pages', 'page_' + fname + '.html')
print('New file:', fname)

# Read the body of the last file
last_file = 'last-page-saved.html'
with open(last_file, 'rb') as f:
    last_file_content = f.read()

with urllib.request.urlopen('https://waukeeschools.org/rtl/covid-19-information-for-families/') as w:
    new_file_content = w.read()
    
    def no_cache_id(txt):
        return txt.split(b'<!-- This website is like a Rocket')[0]
    
    # Check if most of the page is the same
    if no_cache_id(last_file_content) == no_cache_id(new_file_content):
        print('SKIP: No change to page content')
    else:
        print('Saving new file...')
        with open(fname, 'wb') as f:
           f.write(new_file_content)
        with open(last_file, 'wb') as f:
           f.write(new_file_content)
