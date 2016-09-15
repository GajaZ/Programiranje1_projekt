import os
import requests
import sys
import csv

def shrani(url, ime_datoteke, vsili_prenos=False):
    try:
        print('Shranjujem {}...'.format(url), end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)
    with open(ime_datoteke, 'w') as datoteka:
        datoteka.write(r.text)
        print('shranjeno!')


def vsebina_datoteke(ime_datoteke):
    with open(ime_datoteke, encoding="utf8") as datoteka:
        vsebina = datoteka.read()
    return vsebina


def datoteke(imenik):
    return [os.path.join(imenik, datoteka) for datoteka in os.listdir(imenik)]

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def zapisi_tabelo(slovarji, imena_polj, ime_datoteke):
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w') as csv_dat:
        writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)

def zapisi_vrstico(slovar, imena_polj, ime_datoteke):
    with open(ime_datoteke, 'w') as csv_dat:
        writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
        writer.writerow(slovar)
