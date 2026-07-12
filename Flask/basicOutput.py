from flask import Flask, render_template
my_app = Flask("PMKJ")

@my_app.route('/')
@my_app.route('/home')
def home():
    return render_template('home.html')

@my_app.route('/data')
def bbm():
    return 'PMKJ BBM Home Page'

if __name__ == '__main__':
    my_app.run(debug = True)