def HashGen(text):
    newtxt = ''
    if(len(text) == 0):
        return False
    elif(len(text)>140):
        return False
    else:
        text = '#' + text
        text.strip()
        for i in text:
            
            if(i == " "):
                continue
            newtxt = newtxt + i
    return (newtxt)

print(HashGen(" Hello there thanks for trying my Kata"))

print("  Hello there thanks for trying my Kata   ".strip()) 
