from Koncna_verzija import orodja
import re
import csv

#iz GameRankings poberemo stran
orodja.shrani('http://www.gamerankings.com/sites/1188-ign/index.html?platform=19', 'ign_ocene.html')
html_datoteka = 'ign_ocene.html'


vzorec_igra = re.compile(
    r'<td><a href=.*?>(?P<ime>.*?)\s*\(PC\)</a></b>\s*</td>\s*<td>.*?</td>\s*<td>.*?<a.*?</td>\s*<td>(?P<ocena_ign>\d\.\d)/10'
)

for ujemanje in re.finditer(vzorec_igra, orodja.vsebina_datoteke(html_datoteka)):
    csv_datoteka = html_datoteka.replace('.html', '.csv')
    imena_polj = ['ime', 'ocena_ign']
    with open(csv_datoteka, 'w') as csv_dat:
        writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
        writer.writeheader()
        for ujemanje in re.finditer(vzorec_igra, orodja.vsebina_datoteke(html_datoteka)):
            writer.writerow(ujemanje.groupdict())
