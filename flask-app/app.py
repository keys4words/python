from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0: {
        'title': 'Rinova first post',
        'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }
}



@app.route('/')
def home():
    return 'Hello, world'


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.jinja2', message=f'A post with id{post_id} was not found!')
    return render_template('post.jinja2', post=post)

if __name__=='__main__':
    app.run(debug=True)