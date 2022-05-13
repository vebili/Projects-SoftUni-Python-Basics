A="Число {}, текст {} и отново число {}"
txt=A.format(123,"Python",321)
print(txt)
txt="Число {0} – това е {0:b} или {0:x}".format(42)
print(txt)
txt="Код: {0:05d}, символ: {0:*^5c}".format(65)
print(txt)
txt="Число: {:_>+20.3E}".format(123.468)
print(txt)
B="{0:_{2}{1}s}"
num=6
for k in range(1,num+1):
    print(B.format("*",k,">"),end="")
    print(" "*(2*(num-k)),end="")
    print(B.format("*",k,"<"))
