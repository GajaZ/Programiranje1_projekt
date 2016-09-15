from Koncna_verzija import orodja
import re
import csv


#orodja.shrani('http://steamspy.com/', 'steam_zanri/steam_podatki.html')

regex_url_kategorije = re.compile(r'"">\s*<a href="(?P<url>/genre/(?P<kat>.*?))">(?P<kategorija>.*?)</a>')

#NE DELA, KER IMAJO ZAVAROVANE PODATKE...NEKAKO
#for ujemanje in re.finditer(regex_url_kategorije, vsebina_datoteke('steam_podatki.html')):
#    url = 'http://steamspy.com{}'.format(ujemanje.group('url'))
#    ime_datoteke = 'steam_podatki/{}.html'.format(ujemanje.group('kategorija'))
#    shrani(url, ime_datoteke)

regex_igra = re.compile(r'<td data-order="(?P<ime>.*?)"><a.*?</td>\s*<td class="treleasedate" data-order="(?P<datum_izdaje>.*?)">.*?</td>\s*.*?>\$(?P<cena>.*?)</td>.*?">(?P<ocena_steam>.*?)\s*\(.*?="(?P<stevilo_igralcev>\d*)">.*?data-order="\d*">(?P<igralni_cas>.*?)\s*\(')


#iz html datotek naredimo csv

# for html_datoteka in orodja.datoteke('steam_zanri'):
#      if html_datoteka[-4:] == '.csv':
#          continue
#      csv_datoteka = html_datoteka.replace('.html', '.csv')
#      imena_polj = ['ime', 'datum_izdaje', 'cena', 'ocena_steam', 'stevilo_igralcev', 'igralni_cas']
#      with open(csv_datoteka, 'w', encoding = "utf8") as csv_dat:
#          writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
#          writer.writeheader()
#          for ujemanje in re.finditer(regex_igra, orodja.vsebina_datoteke(html_datoteka)):
#              writer.writerow(ujemanje.groupdict())

#zddruzimo vse v eno

with open('zdruzeno_zanri.csv','w') as fout:
    wtr = csv.writer(fout)
    wtr.writerow(('ime', 'zanr','datum_izdaje','cena','ocena_steam','stevilo_igralcev'))
    for file in orodja.datoteke('steam_zanri'):
        if file[-4:] == 'html':
            continue
        izraz = file.title()
        print(izraz)
        reg_izraz = re.compile(r'\\(?P<zanr>.*?)\.Csv')
        for ujemanje in re.finditer(reg_izraz, izraz):
            dict = ujemanje.groupdict()
            ime_zanra = dict.get('zanr')
            print(ime_zanra)
            with open(file, 'r') as f:
                rdr = csv.reader(f)
                f.__next__()
                for line in rdr:
                    if any(field.strip() for field in line):
                        wtr.writerow((line[0], ime_zanra, line[1], line[2], line[3], line[4]))
