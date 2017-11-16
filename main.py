from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return 'Method used: {}'.format(request.method)

@app.route('/bacon', methods=['GET','POST'])
def bacon():
	if request.method == 'POST':
		return 'Method used: {}'.format(request.method)
	return 'Method used: {}'.format(request.method)


# @app.route('/about/')
# def about():
# 	return 'This is the about page'

# @app.route('/profile/<username>')
# def profile(username):
# 	return '<h1>The page of {}</h1>'.format(username)


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
# 	return '<h1>Post ID is {}</h1>'.format(post_id)



if __name__ == "__main__":
	app.run(debug=True)