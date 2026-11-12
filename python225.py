def count_char(text,char):
    if text == "":
        return 0
    if text[0] == char:
        count =  1
    else:      
        count =0
    total = count + count_char(text[1:],char)
    return total
text = str(input("enter your text:"))
char = str(input("enter your word:"))
print(count_char(text,char))
    