def add_two_numbers(listNumber1: int, listNumber2: int) -> bool:
    total_sum = int("".join(map(str, listNumber1))) + int("".join(map(str, listNumber2)))
    result = list(str(total_sum))
    result.reverse()
    return result

if __name__ == "__main__":
    numbers1 = [3, 2, 1]
    numbers2 = [3, 2, 1]
    
    result = add_two_numbers(numbers1, numbers2)
    print(result)