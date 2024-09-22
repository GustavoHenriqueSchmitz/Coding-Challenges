def reverseOnlyLetters(text: str) -> bool:
    
    reversed_text_list = []
    for character in text:
        if character.isalpha():
            reversed_text_list.append(character)
    reversed_text_list.reverse()
    
    index = 0
    for character in text:
        if character.isalpha() == False:
            reversed_text_list.insert(index, character)
            index += 1
        else:
            index += 1
            
    return ''.join(reversed_text_list) 

if __name__ == "__main__":
    text = 'a-bC-dEf=ghlj!!'
    
    result = reverseOnlyLetters(text)
    
    print(result)
    