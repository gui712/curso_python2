# Exercise - questions and answers 

questions = [
    {
        "Question": "What is the capital of France?",
        "Options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"], 
        "Answer": "A"
    },
    {
        "Question": "What is the largest planet in our solar system?",
        "Options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"], 
        "Answer": "B"
    },
    {
        "Question": "Who wrote 'To Kill a Mockingbird'?",
        "Options": ["A) Harper Lee", "B) Mark Twain", "C) F. Scott Fitzgerald", "D) Ernest Hemingway"], 
        "Answer": "A"
    },
    {
        "Question": "What is the chemical symbol for water?",
        "Options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"], 
        "Answer": "B"
    },
    {
        "Question": "What is the capital of Japan?",
        "Options": ["A) Seoul", "B) Beijing", "C) Tokyo", "D) Bangkok"], 
        "Answer": "C"
    },
    {
        'Question': 'What is 2 + 2?', 
        'Options':['A) 1', 'B) 3', 'C) 4', 'D) 5'],
        'Answer': 'C'
    },
    {
        'Question': 'What is 5*5?',
        'Options': ['A) 25', 'B) 55', 'C) 10', 'D) 51'],
        'Answer': 'A'
    },
    {
        'Question': 'What is 10/2?',
        'Options': ['A) 4', 'B) 5', 'C) 10', 'D) 2'],
        'Answer': 'B'
    }
]

qtd_acertos = 0 
for question in questions:
    print('Question: ', question['Question'])
    print()

    for i, option in enumerate(question['Options']):
        print(option)
    
    choose = input('Choose an option (A, B, C, D): ').strip().upper()
    if choose == question['Answer']:
        qtd_acertos += 1
        print('Correct!')
    else:
        print('Incorrect! The correct answer is:', question['Answer'])



    print()

print('You got', qtd_acertos, 'out of', len(questions), 'correct.')