def getMostRepeatedCharacter(text: str) -> bool:
    
    quantidades = {}
    for character in text:
        if character.isalpha():
            if character in quantidades.keys():
                quantidades[character] += 1
            else:
                quantidades[character] = 1
    
    most_repeated = { 'quantidade': 0, 'nome': '' }
    for key, value in quantidades.items():
        if value > most_repeated['quantidade']:
            most_repeated = { 'quantidade': value, 'nome': key }
    
    return most_repeated

if __name__ == "__main__":
    text = 'abcddefda1111133333333'
    
    result = getMostRepeatedCharacter(text)
    
    print(result)