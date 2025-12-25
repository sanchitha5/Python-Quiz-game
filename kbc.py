questions = [ 
    ["1. Which is the capital of India: ", "Mumbai", "New Delhi", "Bangalore", "Gujarat", 2 ],
    ["2. National Animal Of India: ", "Lion", "Elephant", "Tiger", "Dog", 3 ],
    ["3. Who is the current Prime Minister of India: ", "Narendra Modi", "Indira Gandhi", "Shri Atal Bihari Vajpayee", "Jawaharlal Nehru", 1],
    ["4. How many days are there in a week: ", "5 days", "9 days", "3 days", "7 days", 4],
    ["5. Which festival is called the 'Festival Of Colours': ", "Holi", "Diwali", "Ganpati", "Christmas", 1],
    ["6. How many sides are there in a triangle: ", "Two", "Four", "Three", "One", 3],
    ["7. Sun rises in the: ", "East", "West", "South", "North", 1],
    ["8. How many minutes are there in an hour: ", "30 minutes", "60 minutes", "40 minutes", "120 minutes", 2],
    ["9. Name the planet nearest to the Earth: ", "Venus", "Mercury", "Pluto", "Saturn", 1],
    ["10. Which is the tallest mountain in the world: ", "Mount Fiji", "Mount Kilimanjaro", "Mount Rainier", "Mount Everest", 4],
    ["11. Rainbow consists of how many colours: ", "5 colours", "10 colours", "7 colours", "9 colours", 3],
    ["12. What is the currency of India: ", "Yen", "Dollar", "Franc", "Rupee", 4],
    ["13. Which element has the chemical symbol 'O': ", "Nitrogen", "Oxygen", "Octanes", "Osmium", 2],
    ["14. Who was the first man to step on the moon: ", "Buzz Aldrin", "Neil Armstrong", "John Glenn", "Alan Shepard", 2],
    ["15. Who painted the Mona Lisa: ", "Leonardo da Vinci", "Picasso", "Jackson Pollock", "Johannes Vermeer", 1]
]

levels = [ 1000, 2000, 3000, 5000, 100000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money=0
for i in range(0, len(questions)):

    question=questions[i]
    print (f" \n \n { question[0]}")
    print ( f" Question For Rs. {levels[i]}")
    print ( f" 1. { question[1]}" )
    print ( f" 2. { question[2]}" )
    print ( f" 3. { question[3]}" )
    print ( f" 4. { question[4]}" )

    reply = int(input(" Enter your answer (1-4) or 0 to quit :\n"))
    if(reply == 0):
        money = levels[i-1]
        break

    if reply == int(question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")

        if(i == 4):
             money = 1000
        elif(i == 9):
            money = 10000
        elif(i == 13):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong Answer!!")
        break

print( f" Congratulations, Your take home money is {money}")



