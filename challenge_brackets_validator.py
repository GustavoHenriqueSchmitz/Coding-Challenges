if __name__ == "__main__":
    brackets_string = input("Brackets String: ")
    brackets = ["()", "[]", "{}"]
    
    while True:
        for bracket in brackets:
            brackets_string = brackets_string.replace(bracket, "")
        
        if len(brackets_string) == 0:
            print("valid")
            break
        elif all(bracket not in brackets_string for bracket in brackets):
            print("invalid")
            break
