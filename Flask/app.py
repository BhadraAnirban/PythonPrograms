from flask import Flask, make_response, render_template, request, redirect, url_for
from loginapi import login_api

app = Flask(__name__)
app.register_blueprint(login_api)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['GET'])
def data(): 
    # Get the query parameters from the request
    param1 = request.args['param1']
    param2 = request.args.get('param2')
    return f"Received parameters: param1={param1}, param2={param2}"


#Dynamic route parameters:
# http://127.0.0.1:5000/user/bbm
@app.route('/user/<username>')
def show_user_profile(username):
    # Show the user profile for that user
    return f'User {username}'



@app.route('/post/<int:post_id>/<string:post_title>')
def show_post_title(post_id, post_title):
    # Show the post with the given id, the id is an integer
    return f'Post {post_id}: {post_title}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # response object with status code 200
    res = make_response(f'<b>Post value: <i>{post_id}</i></b>')
    res.status_code = 200
    return res





## from the command line run the app with:  
# flask run
## or with debug mode enabled run the app with:
# flask --app app --debug run

## otherwise uncomment this line to run the app in debug mode with command:  python app.py
if __name__ == '__main__':
     app.run(debug=True)   


