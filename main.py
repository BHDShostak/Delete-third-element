
def kill3charter(txt):
    OutText = ''
    for i, char in enumerate(txt):
        if i % 3 != 0:
            OutText += char 
    return OutText

txt = input() #input the text, who need a delete every 3-th charachter

l = len(txt) #count a long of text

print(kill3charter(txt)) # output text to consumer


