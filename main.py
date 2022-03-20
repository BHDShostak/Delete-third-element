
def kill3charter(txt):
    OutText = ''
    for i in range (0,l):
        if i % 3 != 0:
            OutText += txt[i]
    return OutText

txt = input () #input the text, who need a delete every 3-th charachter

l = len (txt) #count a long of text

print(kill3charter(txt)) # output text to consumer


