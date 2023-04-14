code = ["d", "c", "b", "a"]
answer = ["d", "b", "a", "a"]

correct_places = [0, 3]
wrong_places = []

for index_answer in range(len(answer)):
    for index_code in range(len(code)):
        if answer[index_answer] == code[index_code] and index_code not in correct_places and index_answer not in correct_places and index_code not in wrong_places:
            wrong_places.append(index_code)
            break

print(wrong_places)