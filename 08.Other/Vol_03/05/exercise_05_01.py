print("** Opening and closing the file")
txt = open("text.txt", "r", encoding='utf-8')
txt.close()

# Четене символ по символ
print("** Reading by char")
txt = open("text.txt", "r")
print(txt.read(1))
print(txt.read(2))
print(txt.read(6))
txt.close()

# Пример за определяне на кодировката
print("** Reading by char with charset definition")
txt = open("text.txt", "r", encoding='utf-8')
print(txt.read(1))
print(txt.read(2))
print(txt.read(6))
txt.close()

# Четене на целия файл
print("** Reading the whole file")
txt = open("text.txt", "r", encoding='utf-8')
content = txt.read()
print(content)
txt.close()

# Четене на ред от файл символ по символ
print("** Reading the line from the file character by char ")
txt = open("text.txt", "r", encoding='utf-8')
print(txt.readline(1))
print(txt.readline(5))
txt.close()

# Четене на целия ред
print("** Reading the whole line")
txt = open("text.txt", "r", encoding='utf-8')
print(txt.readline())       # Ред 1
print(txt.readline())       # Ред 2
txt.close()

# Четене на целия файл в списък
print("** Reading the entire file to the list ")
txt = open("text.txt", "r", encoding='utf-8')
lines = txt.readlines()

print(lines)
print(len(lines))
for line in lines:
    print(line)

txt.close()

# Четене на файла ред по ред
print("** Read the file in-line:")
txt = open("text.txt", "r", encoding='utf-8')
for line in txt:
      print(line)
txt.close()
