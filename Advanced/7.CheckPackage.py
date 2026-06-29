from MyPackage.Module1 import add
from MyPackage.Module2 import MyClass2
print('Adition value: ', add(2, 26))

myclass2Obj = MyClass2()
print('myclass2Obj info: ', myclass2Obj)
print('myclass2Obj Multi: ', myclass2Obj.multi(2, 26))

#The Python module should be packaged in a directory with __init__.py in the same directory
#The in the parent directory console(cmd) type- Python and enter