##############################################CREATED BY MUHAMMAD HANAN ASGHAR##################################
#Library To Load Json in Python
import json
#Library To get Similarity between two Strings
from difflib import get_close_matches



#This line is to Convert or Load the Json file to Python Dictionary
data = json.load(open('data.json'))

#Function to Search Word
def vocabFunc(word):
    listy = []
    #Convert word to lower
    word = word.lower()
    try:
        if word not in data.keys():
            #Logic To get Similarity
            a = get_close_matches(word,data.keys())
            b = input(f'Are You Thinking About Anyone of these : {a} : If this then Enter What you want to Search :  ')
            c = data[b.lower()]
            #Logic To Print The Answer
            print(f"{b.capitalize()} : ")
            #For iterating the Object
            if type(c) == type(listy):
                #To Check if it is type list or not
                for item in c:
                    print(f"{item.capitalize()}")
            else:
                print(f"{c.capitalize()}")
        else:
            a = data[word.lower()]
            print(f"{word.capitalize()} : ")
            #For iterating The Object
            if type(a) == type(listy):
                #To Check if it is type list or not
                for item in a:
                    print(f"{item.capitalize()}")
            else:
                print(f"{a.capitalize()}")

    except:
        print('This Word is Not Found,Please Enter Something Else...')

#Line to get input from user
user_input = input('Enter Word : ')
vocabFunc(user_input)

##############################################CREATED BY MUHAMMAD HANAN ASGHAR##################################
