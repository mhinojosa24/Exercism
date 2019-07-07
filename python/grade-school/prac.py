

def add_person():
    dic = {}
    for num in range(1, 13):
        if num not in dic:
            dic[num] = [1, 9, 4]
    # return dic.values()
    result = dic[3]

    return sorted(result)
print(add_person())
