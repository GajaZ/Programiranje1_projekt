from Koncna_verzija import orodja
import re
import csv

with open('steam_distribucije/zdruzeno_podjetja.csv','w') as fout:
    wtr = csv.writer(fout)
    wtr.writerow(('ime', 'podjetje', 'igralni_cas'))
    for csv_dat in orodja.datoteke('steam_distribucije'):
        izraz = csv_dat.title()
        reg_izraz = re.compile(r'\\(?P<podjetje>.*?)\.Csv')
        for ujemanje in re.finditer(reg_izraz, izraz):
            dict = ujemanje.groupdict()
            ime_podjetja = dict.get('podjetje')
            with open(csv_dat, 'r') as f:
                rdr = csv.reader(f)
                f.__next__()
                for line in rdr:
                    wtr.writerow((line[1], ime_podjetja, line[6]))