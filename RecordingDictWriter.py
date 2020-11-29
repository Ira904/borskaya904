import csv
 
with open('RecordingDictWriter.csv', 'w') as csvfile:
    fieldnames = ['credit ', 'cent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
 
    writer.writeheader()
    writer.writerow({'credit ': 'Consumer credit', 'cent': '9.9%'})
    writer.writerow({'credit ': 'business Loan',
                     'cent': '17%'})
    writer.writerow({'credit ': 'education Loan', 'cent': '3%'})
    writer.writerow({'credit ': 'mortgage', 'cent': '6.6%'})
 
print("Writing complete")