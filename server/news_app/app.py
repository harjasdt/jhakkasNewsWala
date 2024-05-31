from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'title': 'India Tomorrow',
            'author': 'John Doe',
            'date': 'May 30, 2024',
            'content': 'Punjab Lok Sabha Election 2024 Exit Poll and Result: Date, time, where to watch Punjab Exit Poll predictions',
            'image': url_for('static', filename='static/img1.jpg')
        },
        {
            'title': 'Deccan Bird',
            'author': 'Jane Doe',
            'date': 'May 31, 2024',
            'content': 'Lok Sabha Elections 2024 | Stage set for polling in 13 Punjab seats',
            'image': url_for('static', filename='static/img1.jpg')
        }
    ]
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = {
        'title': f'Post {post_id}',
        'author': 'John Doe',
        'date': 'May 30, 2024',
        'content': f'This is the content of post {post_id}.',
        'image': 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fthumbnails%2F002%2F618%2F581%2Fsmall%2Fwoman-puts-a-ballot-paper-in-voting-box-on-red-background-elections-in-the-united-states-photo.jpg&tbnid=L_U5TL0uYV3LyM&vet=10CBQQxiAoB2oXChMIyK_esqS3hgMVAAAAAB0AAAAAEAc..i&imgrefurl=https%3A%2F%2Fwww.vecteezy.com%2Ffree-photos%2Fvote&docid=OezhjjVrHgDyCM&w=300&h=200&itg=1&q=election%20jpg&ved=0CBQQxiAoB2oXChMIyK_esqS3hgMVAAAAAB0AAAAAEAc'
    }
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
