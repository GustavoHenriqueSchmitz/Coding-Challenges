def reverseOnlyLetters(points: str) -> bool:
    
    index = 0
    while index < len(points):
        if points[index] == "+":
            points[index] = (int(points[index-1]) + int(points[index-2]))
            index += 1
        elif points[index] == "D":
            points[index] = int(points[index-1]) * 2
            index += 1
        elif points[index] == "C":
            del points[index]
            del points[index-1]
            index -= 1
        else:
            index += 1
            
    score = 0
    for point in points:
        score += int(point)
        
    return score

if __name__ == "__main__":
    points = ["1"]
    result = reverseOnlyLetters(points)
    print(result)
