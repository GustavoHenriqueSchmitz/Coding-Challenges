def reverseOnlyLetters(text: str) -> bool:
    splited_text = list(text)
    reverted_list = [None] * len(splited_text)
    
    for index, character in enumerate(splited_text):
        if character.isalpha() == False:
            reverted_list[index] = character
    
    index_splited_list = 0
    index_reverted_list = -1
    while True:
        if index_splited_list >= len(splited_text):
            return "".join(reverted_list)
        
        character = splited_text[index_splited_list]
        if character.isalpha() == True:
            if reverted_list[index_reverted_list] == None:
                reverted_list[index_reverted_list] = character
                index_reverted_list -= 1
                index_splited_list += 1
            else:
                index_reverted_list -= 1
                continue
        else:
            index_splited_list += 1
            continue
    
if __name__ == "__main__":
    text = 'a-bC-dEf=ghlj!!'
    result = reverseOnlyLetters(text)
    print(result)
    