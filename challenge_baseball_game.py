def calPoints(scores) -> int:
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
            if deleted_score != None:
                formatted_scores.append(deleted_score)
                deleted_score = None
            else:
                deleted_score = formatted_scores[-1]
                del formatted_scores[-1]
    final_result = 0
    for score in formatted_scores:
        final_result += score
    return final_result

if __name__ == '__main__':
    line = input()
    scores = list(line.strip())
    print(calPoints(scores))