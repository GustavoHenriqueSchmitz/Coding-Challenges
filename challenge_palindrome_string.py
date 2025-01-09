def findPalindromeString(string):
    # Function to validate if a found palindrome string is the longest found already
    def checkIsValidPalindrome():
        if len(palindrome_string) > 2 and len(palindrome_string) > len(longest_palindrome_found.replace("none", "")):
            return True
        else:
            return False
    
    # Take letter by letter, goes forming a word and goes checking if it exist in the reverted string
    longest_palindrome_found = "none"
    palindrome_string = ""
    index = 0
    while True:
        if index == len(string):
            if checkIsValidPalindrome():
                longest_palindrome_found = palindrome_string
            break
        
        if palindrome_string + string[index] in string[::-1]:
            palindrome_string += string[index]
            index += 1
            continue
        else:
            if checkIsValidPalindrome():
                longest_palindrome_found = palindrome_string
            palindrome_string = ""
            string = string[1:]
            index = 0
    return longest_palindrome_found

if __name__ == "__main__":
    # Run many test cases
    for test_case in ["hellosannasmith", "abcdefg", "racecar", "aa", "aaa", "madamimadamracecar"]:
        print(findPalindromeString(test_case))
