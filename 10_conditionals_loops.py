"""
© https://sudipghimire.com.np

Conditional and loop Exercises
"""
import math


'''
1.  Write a program to input a number and check whether a number is an integer or not
    hint: you can use isnumeric() function
'''
# Answer
num = input("Enter any number : \t")
if num.isnumeric():
    print(f"{num} is an Integer")
else:
    print(f"'{num}' is not an Integer")


'''
3. from the list below, separate a list that are even and odd and put them into the respective variables

the final output should be:

Odd numbers: [1, 5, 89, 167, 333, 5, 23]
Even numbers: [2, 32, 112, 20]
'''
num = [1, 5, 2, 89, 32, 112, 167, 333, 20, 5, 23]
odd_num = []
even_num=[]
# Answer
for i in num:
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)

print(f"Odd numbers: {odd_num}")
print(f"Even numbers: {even_num}")


'''
4.  Write a program to input 2 different words and find out if the words are Palindrome or not.

    - A word is palindrome if reads the same from both backward and forward.

    Eg: EVE, HANNAH, BOB, ANNA, ROTATOR, REPAPER
________________________________________________________________________
The Output in the console should look like below
________________________________________________________________________
Enter a word: Hannah

Hannah is a palindrome word
________________________________________________________________________
'''
# answer here
word1=input("Enter a  first word to check if it is Palindrome or not : \t ")
word2=input("Enter a  second word to check if it is Palindrome or not : \t ")
word_list=[word1.lower(),word2.lower()]

for word in word_list:
    if word == word[::-1]:
        print(f"{word} is a palindrome word.")
    else:
        print(f"{word} is not a palindrome word.")

'''
word1=input("Enter a  first word to check if it is Palindrome or not : \t ")
#word2=word1[::-1]  ## Alternative Way
#if word1.lower() == word2.lower(): ## Alternative way
if word1.lower() == word1.lower()[::-1]:

    print(f"{word1} is a palindrome word.")
else:
    print(f"{word1} is not a palindrome word.")

'''


'''
5.  Write a program to print the first 20 fibbonnaccii numbers

    The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is
    the sum of the previous two numbers in the sequence.
    eg: 1, 1, 2, 3, 5, 8, 13, ...

    hint: use for loop in range of 20, add a and b and update values of a, b and others if necessary
'''
a = 1
b = 1
count =0 

# answer here
while count < 20:

      count +=1




'''
6.  Write a program to enter a month and day of birth and find out the horoscope of a person:

- Aries: Mar 21 - Apr 19
- Taurus: Apr 20 - May 20
- Gemini: May 21 - Jun 20
- Cancer: Jun 21 - Jul 22
- Leo: Jul 23 - Aug 22
- Virgo: Aug 23 - Sep 22
- Libra: Sep 23 - Oct 22
- Scorpio: Oct 23 - Nov 21
- Sagittarius: Nov 22 - Dec 21
- Capricorn: Dec 22 - Jan 19
- Aquarius: Jan 20 - Feb 18
- Pisces: Feb 19: Mar 20

________________________________________________________________________
The Output in the console should look like below
________________________________________________________________________
Enter your Month and Day of Birth [Eg: Oct 20]: Oct 20

Your Horoscopic Sign is:    Libra
________________________________________________________________________

Hint:
    you can use `split()` function to split words from a string
'''
# date = 'Oct 20'
# month, day = date.split()
# day = int(day)
# print(month,'/', day)

# answer



'''
BONUS QUESTION
1.  Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee
    according to the customer's requirements.

    The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
    Please use the `make_coffee()` function below to prepare a coffee and serve it. below are the conditions:

    1. Espresso
        - price: $2
        - type: hard

    2. Americano
        - price: $2.5
        - type: mild

    3. Cappuccino
        - price: $3
        - type: soft

    The program should be able to ask user to input a number 1, 2 or 3 and display message according to the conditions above.

________________________________________________________________________
The Output in the console should look like below
________________________________________________________________________
Today's Menu:
1. Espresso
2. Americano
3. Cappuccino

Enter Number:   1

Dear Customer, Your Espresso is ready. please pay $2 at the counter.

Quick fact: Espresso is a hard coffee.
________________________________________________________________________
'''
# Answer


'''
BONUS QUESTION
2. Write a program to check whether a number is a special number or not.

   If the sum of the factorial of digits of a number (N) is equal to the number itself,
   the number (N) is called a special number.

Eg: 145 is a special number where, 1! + 4! + 5! = 145

try it with numbers:    145, 1, 35

Hint 1: you can get each digit using a modulus and integer division of a number by 10 until the number is less than 10
    eg: 145
        145//10 = 14        145%10=5                    (5 is ones digit)
        14//10 = 1          14 % 10 = 4                 (4 is tens digit)
        at the end, 1 (which is less than 10)           (1 is hundreds digit)

hint 2: you can use `math.factorial()` to find out factorial of a number.

'''
# answer here

"""
BONUS QUESTION
3.  Hangman Game
    Create a Guessing game that gives you 3 chance for a person to make mistakes
    Use a word "Elephant" for now
________________________________________________________________________
HANGMAN !!

Guess the word:     E _ _ p _ _ n t

Enter the position, and character [eg: 2 l] to fill the blanks

 E _ _ p _ _ n t    ( 0 / 3 mistakes ):     2 l
 E l _ p _ _ n t    ( 0 / 3 mistakes ):     3 a

 E l * p _ _ n t    ( 1 / 3 mistakes ):

 Try your own logig, or ways. we'll be discussing answers for this game.
________________________________________________________________________
"""
actual_word = 'Elephant'
question = 'E _ _ p _ _ n t'
remaining = 'leha'
progress = 'E _ _ p _ _ n t'

mistake = 0

while mistake < 3:
    next_word = input(f' {progress}\t( {mistake} / 3 mistakes ):\t')
    # remaining answer here
