print("🎉 Welcome to Kaun Banega Crorepati! 🎉\n")
print("The total prize for this game is 35000🤑")
# Set of questions
question = [
    {
        "Question": "Which is the easiest programming language: ",
        "options": ["1:Python", "2:Java", "3:C++"],
        "Answer": "1"
    },
    {
        "Question": "Which language is best for game development: ",
        "options": ["1:react.js", "2:C++", "3:HTML"],
        "Answer": "2"
    },
    {
        "Question": "Which function is used to get user input in Python: ",
        "options": ["1:print()", "2:input()", "3:read()", "4:write()"],
        "Answer": "2"
    },
    {
        "Question": "Who created python: ",
        "options": ["1:James Gosling", "2:Bjarne Stroustrup", "3.Microsoft","4.Guido van Rossum"],
        "Answer": "4"
    }
]
i=5000
for k in question:
    # this will print the options
    print(k["Question"])
    for p in k["options"]:
        print(p)
    # This take the input from the user
    t = input("\nEnter your answer: ")
    # This will check if the answer is correct or not
    if t == k["Answer"]:
        print(f"\nRight answer","\n\nCongratulations!🥳 You won ",i,"\n")
        i+= 5000*2 # increase the money
    # If the answer is not this will print and game will end
    else:
        print(f"\n❌ Wrong! The correct answer was {int(k['Answer'])}.")
        break
print("Thank you for playing!")