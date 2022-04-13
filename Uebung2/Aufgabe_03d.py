dictionary = {"Kind": "child", "Kinder": "children", "Schlange": "snake", "Echse": "lizzard", "spielen": "play", "gerne": "like to", "mit": "with", "einer": "a"}

switcheddict = {y:x for x,y in dictionary.items()}

# iterate through the switched dictionary and add the switched key:value pairs to the original dictionary
for i in switcheddict:
    dictionary[i] = switcheddict[i]
print(dictionary)
teststring = "Kinder spielen gerne mit einer Echse ."
teststring = teststring.split()
translated = []

for entry in teststring:
    if entry in dictionary:
        translated.append(dictionary[entry])

buf = translated[1]
translated[1] = translated[2]
translated[2] = buf
translated = " ".join(translated)

print(translated)