def latest(scores):
    return scores[-1]


def personal_best(scores):
    result = sorted(scores)
    print(result)
    return result[-1]


def personal_top_three(scores):
    if len(scores) <= 1:
        return scores
    result = sorted(scores)
    result = result[::-1]
    return result[:3]

scores = [40, 100, 70]
print(personal_top_three(scores))
