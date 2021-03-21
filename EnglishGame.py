import pandas as pd
import csv
csvReaderName = open ('Dictionary.csv')
csvWriterName = open ('Dictionary.csv','a+', newline='')
writer = csv.writer(csvWriterName)
reader = csv.reader(csvReaderName)
print("Write 1 for introduce words to the dictionary or 2 for play the game")
option =input()

dic={}
for row in reader:
    dic[row[0]] = row[1]
#print (dic)
while((option != '1' ) and (option != '2')):
    print(option +"Write 1 for introduce words to the dictionary or 2 for play the game")
    option =input()

if option == '1':
    print("Write only the new word")
    new_word= input()
    print("Writer the meaning")
    meaning = input()
    writer.writerow([new_word,meaning])
    csvWriterName.close()