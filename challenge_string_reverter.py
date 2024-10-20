def reverseOnlyLetters(text: str) -> bool:
    splited_text = list(text)
    reverted_text = [None] * len(splited_text)
    
    for index, character in enumerate(splited_text):
        if character.isalpha() == False:
            reverted_text[index] = character
    
    index_splited_text = 0
    index_reverted_text = -1
    while True:
        if index_splited_text >= len(splited_text):
            return "".join(reverted_text)
        
        character = splited_text[index_splited_text]
        if character.isalpha() == True:
            if reverted_text[index_reverted_text] == None:
                reverted_text[index_reverted_text] = character
                index_reverted_text -= 1
                index_splited_text += 1
            else:
                index_reverted_text -= 1
                continue
        else:
            index_splited_text += 1
            continue

if __name__ == "__main__":
    text = 'a-bC-dEf=ghlj!!'
    result = reverseOnlyLetters(text)
    print(result)
