import random
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
    print("Write the meaning")
    meaning = input()
    if(new_word in dic):
        print("The word already is in the dictionary")
    else:
        writer.writerow([new_word,meaning])


if option == '2':    
    word_selected = random.choice(list(dic)) 
    print ("The word is:"+ word_selected)
    print("Write his translation into spanish")
    user_translation = input()
    if user_translation == dic[word_selected]:
        print("Success! you got it right!")
    else:
        print("Fail :( the translation is: " + dic[word_selected])
 
csvWriterName.close()
csvReaderName.close()