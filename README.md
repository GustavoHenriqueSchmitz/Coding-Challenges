# Coding Challenges

## About the repository
Basically it contains some logical coding challenges i've faced. Creating this to share a little of my logical and problem solving abilities as a software developer.

## Used Technologies
- Python

## About each challenge

### Add two numbers
In this problem, you're given two non-negative integers represented as linked lists. Each node of the linked list contains a single digit, and the digits are stored in reverse order. The goal is to add the two numbers and return the sum as a new linked list, with digits in reverse order as well.

- The function simulates the addition of two numbers by traversing the linked lists simultaneously, handling carry-over just like manual addition.
- As a constraint, neither of the numbers has leading zeros, except the number "0" itself.
- Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: (7 -> 0 -> 8) (since 342 + 465 = 807)

### Baseball Game
You are tasked with calculating the total score of a baseball game. The game has multiple rounds, and in each round, certain operations can modify the score based on the previous rounds.
- Each round can be one of the following operations:
    - An integer representing the score of the current round.
    - "+" which adds the last two scores.
    - "D" which doubles the last score.
    - "C" which removes the previous score.
- The challenge is to apply these operations in order and return the sum of the scores after all operations are complete.
- Example:
Input: ["5", "-2", "4", "C", "D", "+"]
Output: 27
Explanation: This simulates the described operations to achieve the final score​

### Brackets Validator
This challenge involves validating a string composed of different types of brackets ((), [], {}). The goal is to determine if the brackets are correctly balanced, meaning every opening bracket has a corresponding closing bracket in the correct order.
- The string is valid if every opening bracket is matched with the correct closing bracket.
- For example, the string "([{}])" is valid, but "([)]" is not.

### String Reverter
The goal of this challenge is to reverse only the alphabetic characters in a string, while keeping the position of any non-letter characters (such as punctuation or spaces) unchanged.
- The function iterates through the string, identifies alphabetic characters, and then reverses only those characters, leaving non-letters in their original positions.
- Example:
Input: "a-bC-dEf=ghlj!!"
Output: "j-lh-gfE=dCb!!"
- Here, only the letters are reversed while keeping the punctuation and equal signs in place​


## Author
**Gustavo Henrique Schmitz**

**Linkedin:** https://www.linkedin.com/in/gustavo-henrique-schmitz  
**Portfolio:** https://gustavohenriqueschmitz.com  
**Email:** gustavohenriqueschmitz568@gmail.com  
