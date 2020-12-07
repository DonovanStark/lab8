# Donovan Stark(drs474@nau.edu)
import json
import random


def ask(q):
    answer = ''
    print('\n' + q['question'])
    for i in range(q['type']):
        print(q['answers'][i])
    while type(answer) != int or answer > q['type'] or answer < 1:
        try:
            answer = int(input('\nAnswer?:'))
        except ValueError:
            print('Answer must be a number')
        if type(answer) == int and answer > q['type']:
            print('Answer must be a number less than or equal to ' +
                  str(q['type']))
        if type(answer) == int and answer < 1:
            print('Answer must be a number greater than or equal to 1')
    return answer


def check(a, q):
    if a == q['correct']:
        return True
    else:
        return False


def run_game(questions):
    curr = 0
    correct = 0
    while curr < 10:
        question = questions[curr]
        answer = ask(question)
        if check(answer, question) is True:
            correct += 1
            print('\nCorrect answer')
        else:
            print('\nIncorrect answer')
        print('Current total correct answers is:' + str(correct) + '\n')
        curr += 1
    return correct


def main():
    print('Python Trivia Game')
    path = input(
        'Would you like to:\n(P)lay the game\n(V)iew game credits\n(Q)uit\n'
    ).upper()
    if path == 'P' or path == 'PLAY':
        with open('questions.json') as f:
            questions = json.load(f)
        random.shuffle(questions)
        correct = run_game(questions)
        if correct == 10:
            print('Congratulations you got 100% of the questions correct')
        else:
            print('Looks like you missed ' + str(10 - correct) +
                  ' questions.\n' + 'Better luck next time\n')
        return True
    if path == 'V' or path == 'VIEW':
        print('\nPython Trivia Game')
        print('Created by Donovan Stark\n')
        return True
    if path == 'Q' or path == 'QUIT':
        print('\nThanks for playing!')
        return False


while main() is True:
    pass
