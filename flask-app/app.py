from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
posts = {
    0: {
        'post_id': 0,
        'title': 'Rinova first post',
        'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }
}



@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.jinja2', message=f'A post with id{post_id} was not found!')
    return render_template('post.jinja2', post=post)

# @app.route('/post/form')
# def form():
#     return render_template('create.jinja2')

@app.route('/post/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id':post_id, 'title':title, 'content':content}

        return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')

if __name__=='__main__':
    app.run(debug=True)