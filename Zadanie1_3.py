with open("words.txt") as f:
    text = f.read()
    result = max(text.split(), key=len)
    print(result)
