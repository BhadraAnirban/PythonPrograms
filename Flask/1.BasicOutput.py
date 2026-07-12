from flask import Flask
my_app = Flask("PMKJ")

@my_app.route('/')
def bbm():
    print 'PMKJ'

if name == 'main':
    my_app.run(debug = True)