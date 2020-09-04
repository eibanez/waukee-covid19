import datetime
import os.path
import urllib.request

ts = datetime.datetime.utcnow()
fname = str(ts).replace(':', '-').replace(' ', '_')[:19]
fname = os.path.join('pages', 'page_' + fname + '.html')
print(fname)

with urllib.request.urlopen('https://waukeeschools.org/rtl/covid-19-information-for-families/') as w:
    with open(fname, 'wb') as f:
        f.write(w.read())
