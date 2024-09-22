def calPoints(scores) -> int:
    """
    :type ops: List[str] - List of operations
    :rtype: int - Sum of scores after performing all operations
    """
    deleted_score = None
    formatted_scores = []
    for score in scores:
        if score.replace("-", "").isdigit():
            formatted_scores.append(int(score))
            deleted_score = None
        elif score == "+":
            formatted_scores.append(formatted_scores[-1] + formatted_scores[-2])
            deleted_score = None
        elif score == "D":
            formatted_scores.append(formatted_scores[-1] * 2)
            deleted_score = None
        elif score == "C":
            index = scores.index(score)
            if scores[::-1][index-1] == "C" and deleted_score != None:
                formatted_scores.append(deleted_score)
                deleted_score = None
            elif scores[index-1] == "C" and deleted_score == None:
                deleted_score = formatted_scores[-1]
                del formatted_scores[-1]
            else:
                deleted_score = formatted_scores[-1]
                del formatted_scores[-1]
    final_result = 0
    for score in formatted_scores:
        final_result += score
    return final_result

if __name__ == '__main__':
    line = input()
    scores = line.strip().split()

    print(calPoints(scores))