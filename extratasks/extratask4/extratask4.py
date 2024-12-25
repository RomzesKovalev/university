import re
import urllib.request
import csv

site = urllib.request.urlopen('https://msk.spravker.ru/avtoservisy-avtotehcentry')
html_content = site.read().decode()

pattern = r"(?:-link\">)(?P<name>[^<]+)(?:[^o]*[^l]*.*\n *)(?P<address>[^\n]+)(?:\s*.*>\s*.*>\s*.*>\s*<d[^>]*>\s*.*\s*.*>(?P<phone>[^<]+).*>\s*</dl>)?(?:\s*<.*>\s*<.*\s*<.*>(?P<workhour>[^<]+)</dd>)?"
match = re.findall(pattern, html_content)

with open('final_text.csv', 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(['Имя', 'Адрес', 'Номер телефона', 'Часы работы'])
    writer.writerows(match)

matches = re.finditer(pattern, html_content)

for match in matches:
    print("Имя:", match.group('name'))
    print("Адрес:", match.group('address'))
    print("Телефон:", match.group('phone'))
    print("Часы работы:", match.group('workhour'))
    print("\n")