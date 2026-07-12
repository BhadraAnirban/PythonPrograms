# Decorators help in annotating the methods and tell what a particular method is meant for. 
# These are different from comments. This is used by the interpreter while running the code.

def jsonify_decorator(function):
    def modify_output():
        return {"output": function()}
    return modify_output

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)

print(hello())
print(add())