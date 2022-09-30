# Описание на класове:
class Alpha:
    pass
class Bravo:
    pass
class Charlie(Alpha,Bravo):
    pass
class Delta(Bravo):
    pass
class Echo(Charlie,Delta):
    pass
# Йерархия от наследявания:
k=1
for s in Echo.__mro__:
   print("["+str(k)+"]",s.__name__)
   k+=1
