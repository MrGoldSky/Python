# Английский словарь 
MorseCode = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

CodeMorse = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
}


def encode_to_morse(text):
    text = text.lower()
    text = text.split()
    b = []
    for j in range(len(text)):
        for i in text[j]:
            if i in MorseCode:
                b.append(MorseCode[i])
            else:
                return(f"Символ {i} не в таблице значений")
        print(*b)
        b.clear()


def decode_from_morse(code):
    code = code.split()
    b = []
    for i in code:
        if i in code:
            b.append(CodeMorse[i])
        else:
            return(f"Код {i} не в таблице значений")
    print(*b)
    b.clear()


decode_from_morse("... --- ...    ... .- ...- .    --- ..- .-.    ... --- ..- .-.. ...")