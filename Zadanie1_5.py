with open("lorem.txt") as f:
    text = f.read().lower()

    char_list = []
    char_dict = {}

    for i in range (len(text)):
        if text[i] in char_list:
            char_dict[text[i]]+=1
        else:
            if text[i] != " ":
                char_list.append(text[i])
                char_dict[text[i]] = 1


    
    for key, value in char_dict.items():
        print(f"Символ {key} встречается {value} раз")
