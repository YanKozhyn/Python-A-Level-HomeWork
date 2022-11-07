# Переконвертував файл з docx to txt, та відкривав його, о таке слово було: СТРЕЛКИ-БЛИЗНЕЦЫ
# бо коли перебирав файл тільки англ мовую там було слово: SELF-FLAGELLATION,
inputFile = "file_1.txt"
with open(inputFile, 'r', encoding="utf8") as f:
    wordsList = f.read().split()
    longestWordLength = len(max(wordsList, key=len))
    result = str([textword for textword in wordsList if len(textword) == longestWordLength]).upper()
with open(inputFile, 'a', encoding="utf8") as f:
    f.write(result)