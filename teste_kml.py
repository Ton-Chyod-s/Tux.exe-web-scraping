from pykml import parser
import csv
import os
import zipfile


import zipfile

with zipfile.ZipFile(os.path.abspath(' '), 'r') as zip_ref:
    zip_ref.extractall(os.path.abspath(' '))
    

with open(os.path.abspath(' ')) as f:
    doc = parser.parse(f).getroot()

pontos = []
for pm in doc.Placemark:
    coords = pm.Point.coordinates.text.strip().split(',')
    lat, lon = float(coords[1]), float(coords[0])
    descricao = pm.description.text.strip() if pm.description else ''
    pontos.append({'latitude': lat, 'longitude': lon, 'descricao': descricao})

with open('pontos.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['latitude', 'longitude', 'descricao'])
    for ponto in pontos:
        writer.writerow([ponto['latitude'], ponto['longitude'], ponto['descricao']])