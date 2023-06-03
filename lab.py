import random

def capitalsQuiz():
    totalCorrect = 0
    totalIncorrect = 0
    states = [
        {
            "name": "Alabama",
            "capital": "Montgomery"
        }, {
            "name": "Alaska",
            "capital": "Juneau"
        }, {
            "name": "Arizona",
            "capital": "Phoenix"
        }, {
            "name": "Arkansas",
            "capital": "Little Rock"
        }, {
            "name": "California",
            "capital": "Sacramento"
        }, {
            "name": "Colorado",
            "capital": "Denver"
        }, {
            "name": "Connecticut",
            "capital": "Hartford"
        }, {
            "name": "Delaware",
            "capital": "Dover"
        }, {
            "name": "Florida",
            "capital": "Tallahassee"
        }, {
            "name": "Georgia",
            "capital": "Atlanta"
        }, {
            "name": "Hawaii",
            "capital": "Honolulu"
        }, {
            "name": "Idaho",
            "capital": "Boise"
        }, {
            "name": "Illinois",
            "capital": "Springfield"
        }, {
            "name": "Indiana",
            "capital": "Indianapolis"
        }, {
            "name": "Iowa",
            "capital": "Des Moines"
        }, {
            "name": "Kansas",
            "capital": "Topeka"
        }, {
            "name": "Kentucky",
            "capital": "Frankfort"
        }, {
            "name": "Louisiana",
            "capital": "Baton Rouge"
        }, {
            "name": "Maine",
            "capital": "Augusta"
        }, {
            "name": "Maryland",
            "capital": "Annapolis"
        }, {
            "name": "Massachusetts",
            "capital": "Boston"
        }, {
            "name": "Michigan",
            "capital": "Lansing"
        }, {
            "name": "Minnesota",
            "capital": "St. Paul"
        }, {
            "name": "Mississippi",
            "capital": "Jackson"
        }, {
            "name": "Missouri",
            "capital": "Jefferson City"
        }, {
            "name": "Montana",
            "capital": "Helena"
        }, {
            "name": "Nebraska",
            "capital": "Lincoln"
        }, {
            "name": "Nevada",
            "capital": "Carson City"
        }, {
            "name": "New Hampshire",
            "capital": "Concord"
        }, {
            "name": "New Jersey",
            "capital": "Trenton"
        }, {
            "name": "New Mexico",
            "capital": "Santa Fe"
        }, {
            "name": "New York",
            "capital": "Albany"
        }, {
            "name": "North Carolina",
            "capital": "Raleigh"
        }, {
            "name": "North Dakota",
            "capital": "Bismarck"
        }, {
            "name": "Ohio",
            "capital": "Columbus"
        }, {
            "name": "Oklahoma",
            "capital": "Oklahoma City"
        }, {
            "name": "Oregon",
            "capital": "Salem"
        }, {
            "name": "Pennsylvania",
            "capital": "Harrisburg"
        }, {
            "name": "Rhode Island",
            "capital": "Providence"
        }, {
            "name": "South Carolina",
            "capital": "Columbia"
        }, {
            "name": "South Dakota",
            "capital": "Pierre"
        }, {
            "name": "Tennessee",
            "capital": "Nashville"
        }, {
            "name": "Texas",
            "capital": "Austin"
        }, {
            "name": "Utah",
            "capital": "Salt Lake City"
        }, {
            "name": "Vermont",
            "capital": "Montpelier"
        }, {
            "name": "Virginia",
            "capital": "Richmond"
        }, {
            "name": "Washington",
            "capital": "Olympia"
        }, {
            "name": "West Virginia",
            "capital": "Charleston"
        }, {
            "name": "Wisconsin",
            "capital": "Madison"
        }, {
            "name": "Wyoming",
            "capital": "Cheyenne"
        }
    ]

    random.shuffle(states)

    for state in states:
        print(f'What is the capital of this state: {state["name"]}')
        if(("correct" in state) == False):
            state["correct"] = 0
        if(("incorrect" in state) == False):
            state["incorrect"] = 0   
        userInput = input()
        if(userInput == state['capital']):
            totalCorrect += 1
            state["correct"] += 1
            print('Correct!')
            print(f'Total Correct Answers: {totalCorrect} Total Incorrect Answers: {totalIncorrect}')
        else:
            totalIncorrect += 1
            state["incorrect"] += 1
            print('Incorrect!')
            print(f'Total Correct Answers: {totalCorrect} Total Incorrect Answers: {totalIncorrect}')
    
    print(states)
    print("Would you like to play again?")
    userInput = input()
    if(userInput == "yes"):
        capitalsQuiz()
    else:
        print("Thanks for playing!")

capitalsQuiz()