def calculate_love_score(name1, name2):
    name_str = (name1 + name2).strip().lower()

    sum_num_true = 0
    for letter_in_true in "true":
        for letter_in_name_str in name_str:
            if letter_in_true == letter_in_name_str:
                sum_num_true += 1
    
    sum_num_love = 0
    for letter_in_love in "love":
        for letter_in_name_str in name_str:
            if letter_in_love == letter_in_name_str:
                sum_num_love += 1
    
    score = int(f"{sum_num_true}{sum_num_love}")      
    return score

print(calculate_love_score('karoly hornyak', 'joanna sorichta'))
