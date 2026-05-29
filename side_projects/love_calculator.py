def calculate_love_score(name1, name2):
    combined_names = name1+name2
    
    true_total = 0
    for letters in "true":
        true_total += combined_names.count(letters)
    
    love_total = 0
    for letters in "love":
        love_total += combined_names.count(letters)
        
    score = int(str(true_total) + str(love_total))
    print(score)
    
calculate_love_score("boy", "girl")

# This is a hard one as I didn't know you can hardcode strings into a for loop.