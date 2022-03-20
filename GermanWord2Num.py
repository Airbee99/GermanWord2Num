def GermanWord2Number(textnum, numwords={}):

    # POSSIBLE NUMBERWORDS
    units = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf"]
    tens = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achzig", "neunzig"]
    scales = ["hundert", "tausend", "million", "milliarde", "billion", "billiarde"]


    # REPLACE SOME NUMBER WORDS
    if "eins" in textnum:
        textnum = textnum.replace("eins", "ein")
    elif "eine" in textnum:
        textnum = textnum.replace("eine", "ein")
    elif "millionen" in textnum:
        textnum = textnum.replace("millionen", "million")
    elif "milliarden" in textnum:
        textnum = textnum.replace("milliarden", "milliarde")
    elif "billionen" in textnum:
        textnum = textnum.replace("billionen", "billion")
    elif "billiarden" in textnum:
        textnum = textnum.replace("billiarden", "billiarde")


    # SPLIT NUMBER WORDS
    for UnitWord in units:
        if UnitWord in textnum:
            textnum = textnum.replace(UnitWord, " "+UnitWord+" ")
    for TensWord in tens:
        if TensWord in textnum:
            if TensWord != "":
                textnum = textnum.replace(TensWord, " " + TensWord + " ")
    for ScalesWord in scales:
        if ScalesWord in textnum:
            textnum = textnum.replace(ScalesWord, " " + ScalesWord + " ")

    if " zig" in textnum:
        textnum = textnum.replace(" zig", "zig")
    if " ßig" in textnum:
        textnum = textnum.replace(" ßig", "ßig")
    if "komma" in textnum:
        textnum = textnum.replace("komma", " komma ")



    if not numwords:

        numwords["komma"] = (1, -1)
        numwords["und"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    comma = False
    for word in textnum.split():
        if word not in numwords:
            continue

        scale, increment = numwords[word]
        if increment == -1:
            current = current * scale
            current = str(current)
            current + "."
            current = float(current)
            comma = True
        else:
            if comma == True:
                current = float(current) * scale + increment*0.1
                comma = False
            else:
                current = float(current) * scale + increment

        if scale > 100:
            result += current
            current = 0


    return result + current



# EXAMPLE: "zweihundert" , "zwei hundert"
# EXAMPLE FOR COMMA: "dreikommazwei" , "drei komma zwei" --> WORKS ONLY FOR ONE NUMBER AFTER COMMA
print(GermanWord2Number("vierundzwanzigkommadrei"))
