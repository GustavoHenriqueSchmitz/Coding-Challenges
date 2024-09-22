def add_two_numbers(listNumber1: int, listNumber2: int) -> bool:
    number1 = int(''.join(map(str, listNumber1)))
    number2 = number = int(''.join(map(str, listNumber2)))
    summed_numbers = number1 + number2
    
    final_result = ''
    for number in reversed(str(summed_numbers)):
        final_result += number
    
    return int(final_result)

if __name__ == "__main__":
    number1 = [0]
    number2 = [0]
    
    result = add_two_numbers(number1, number2)
    
    print(result)