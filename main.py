import csv
import os
import re
import optparse
import requests
import uuid
from weasyprint import HTML, CSS

parser = optparse.OptionParser()
parser.add_option('-t', '--template', type='string', default='template.html')
parser.add_option('-c', '--csv', type='string', default='students.csv')
parser.add_option('-o', '--output', type='string', default='output.csv')

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
        writer = csv.writer(open(options.output, 'w'))
        header = next(reader)
        writer.writerow(header)
        text = htmlfile.read()
        for index, row in enumerate(reader):
            html = text
            url = f'certificate/{uuid.uuid4()}.pdf'
            for i in range(len(header)):
                html = html.replace("{{" + header[i] + "}}", row[i])
                if (header[i] == 'link'):
                    row[i] = url
            html = HTML(string=html, base_url='.')
            writer.writerow(row)
            css = CSS(string='''@page { size: A4; margin: 0cm }''')
            html.write_pdf(url, stylesheets=[css])