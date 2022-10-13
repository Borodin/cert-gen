import csv
import os
import re
import optparse
import requests
from weasyprint import HTML, CSS

parser = optparse.OptionParser()
parser.add_option('-t', '--template', type='string', default='template.html')
parser.add_option('-c', '--csv', type='string', default='students.csv')

options, arguments = parser.parse_args()

if not os.path.exists('certificate'):
    os.makedirs('certificate')

if re.search('google.com', options.csv):
    id = re.search('\/d\/(.+?)\/', options.csv).group(1)
    file = requests.get(f"https://docs.google.com/spreadsheet/ccc?key={id}&output=csv").content
    options.csv = 'temp.csv'
    with open(options.csv, 'wb') as f:
        f.write(file)

with open(options.template) as htmlfile:
    with open(options.csv, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        text = htmlfile.read()
        for index, row in enumerate(reader):
            html = text
            for i in range(len(header)):
                html = html.replace("{{" + header[i] + "}}", row[i])
            html = HTML(string=html, base_url='.')
            css = CSS(string='''@page { size: A4; margin: 0cm }''')
            html.write_pdf(f"certificate/cert_{index + 1}.pdf", stylesheets=[css])
