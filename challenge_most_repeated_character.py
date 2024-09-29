def getMostRepeatedCharacter(text: str) -> bool:
    characters_quantity = {}
    for character in text:
        if character.isalpha():
            if character not in characters_quantity:
                characters_quantity[character] = 1
            else:
                characters_quantity[character] += 1
    
    most_repeated_character = {"character": "", "total": 0}
    for character, total in characters_quantity.items():
        if total > most_repeated_character["total"]:
            most_repeated_character = {"character": character, "total": total}
    return most_repeated_character["character"]

if __name__ == "__main__":
    text = 'abcddefda1111133333333'
    result = getMostRepeatedCharacter(text)
    print(result)