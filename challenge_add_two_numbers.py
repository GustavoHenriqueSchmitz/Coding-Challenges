def add_two_numbers(listNumber1, listNumber2):
    listNumber1.reverse()
    listNumber2.reverse()
    
    number1 = "".join(map(str, listNumber1))
    number2 = "".join(map(str, listNumber2))
    
    total_sum = int(number1) + int(number2)
    result = list(str(total_sum))
    result.reverse()
    return result

if __name__ == "__main__":
    numbers1 = list(input("Number 1: "))
    numbers2 = list(input("Number 2: "))
    result = add_two_numbers(numbers1, numbers2)
    print(result)
