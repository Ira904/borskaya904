import csv
 
myData = [["credit", ";cent"],
          ['Consumer credit', '9.9%'],
          ['business Loan', '17%'],
          ['mortgage', '3%']]
 
myFile = open('RecordingWriter.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(myData)
     
print("Writing complete")