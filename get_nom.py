from os import listdir
import urllib.request
import pdb
import csv

def header(position):
    s = '<div class="panel panel-default">' +\
        '<div class="panel-heading">' +\
        position +\
        '</div>' +\
        '<ul class="list-group">'

    print(s)

def item(name, filename):
    s = '<li class="list-group-item">' +\
        '<a href="w1papers/%s">%s</a>' % (filename, name) +\
        '</li>'
    print(s)

def end():
    s = ' </ul> </div>'
    print(s)

excuse = [
        'Farquaad',
        'Alexander Sapp',
        'Pierre Kochel',
        'Cindy Wu',
        'Ted Smith-Windsor',
        'Michael Johnston'
]

url = 'https://docs.google.com/spreadsheets/d/1v9SOc16oCzFc5lAJkVmbrHGAwzJjPgdMPN69lOuULp4/pub?output=csv'

noms = {}
with urllib.request.urlopen(url) as sheet:
    cr = csv.reader(sheet.read().decode('utf-8').splitlines())
    raw_noms = list(cr)

    pos_i = raw_noms[0].index('Position?')
    name_i = raw_noms[0].index('Name (as will appear in ballot)')

    c = 0
    for row in raw_noms[1:]:
        position = row[pos_i].strip()
        name = row[name_i].strip()

        skip = False
        for n in excuse:
            if n in name:
                skip = True

        if skip:
            continue

        if position not in noms:
            noms[position] = set()
        noms[position].add(name)
        c += 1

    paper_files = listdir('w1papers')
    p = 0
    for key in noms:
        header(key)
        # print(key)
        # pdb.set_trace()

        for name in noms[key]:

            has_paper = False
            for paper in paper_files:
                paper_name = ' '.join(paper.strip('.pdf').split('_')[1:])
                if paper_name == name:
                    p += 1
                    break

            item(name, paper)
            # print('-', name, paper)
        end()

    # print('Total candidates:', c)
    # print('Total papers:', p)
