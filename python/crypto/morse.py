t = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--．": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "---...": ":",
    "--..--": ",",
    "-.-.-.": ";",
    "..--..": "?",
    "-...-": "=",
    ".----.": "'",
    "-..-.": "/",
    "-.-.--": "!",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    "-.--.": "(",
    "-.--.-": ")",
    "...-..-": "$",
    "....": "&",
    ".--.-.": "@",
    ".-.-.": "+",
}


def foo(c: str, split_str):
    m = ""
    for i in c.split(split_str):
        m += t.get(i)
    return m


c = "...../-..../----./...../-----/-----/-..../--.../....-/....-/....-/-----/...--/---../..---/--.../.----/---../-----/.----/..---/...../--.../....-/....-/...../----./...../---../...../.----/...--/..---/----./---../..---/-..../---../----./.----/..---/--.../--.../..---/.----/--.../-..../.----/---../---../---../..---/---../--.../---../--.../...../---../----./--.../----./---../-----/...--/...../-..../..---/..---/----./-----/..---/--.../....-/...--/.----/.----/....-/-..../---../--.../-----/-..../-----/.----/..---/----./--.../----./....-/...--/....-/-..../..---/--.../...--/....."
m = foo(c, "/")
print(m)
