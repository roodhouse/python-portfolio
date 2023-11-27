# create flask app - done
# create template base files
    # create static css 
# bring images into static
# connect it
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy()
db.init_app(app)

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

# seed db
# html = Skills(
#     title = 'HTML',
#     img_url = 'static/images/html.png'
# )

# css = Skills(
#     title = 'CSS',
#     img_url = 'static/images/css.png'
# )

# javascript = Skills(
#     title = 'JavaScript',
#     img_url = 'static/images/javascript.png'
# )

# react = Skills(
#     title = 'React',
#     img_url = 'static/images/react.png'
# )

# node = Skills(
#     title = 'Node',
#     img_url = 'static/images/node.png'
# )

# aws = Skills(
#     title = 'AWS',
#     img_url = 'static/images/aws.png'
# )

# github = Skills(
#     title = 'Github',
#     img_url = 'static/images/github.png'
# )

# tailwind = Skills(
#     title = 'Tailwind',
#     img_url = 'static/images/tailwind.png'
# )

# python = Skills(
#     title = 'Python',
#     img_url = 'static/images/python.png'
# )

# flask = Skills(
#     title = 'Flask',
#     img_url = 'static/images/flask.svg'
# )

# mongo = Skills(
#     title = 'MongoDB',
#     img_url = 'static/images/mongo.png'
# )

# mysql = Skills(
#     title = 'MySQL',
#     img_url = 'static/images/mysql.svg'
# )

# with app.app_context():
#     db.session.add(html)
#     db.session.add(css)
#     db.session.add(javascript)
#     db.session.add(react)
#     db.session.add(node)
#     db.session.add(aws)
#     db.session.add(github)
#     db.session.add(tailwind)
#     db.session.add(python)
#     db.session.add(flask)
#     db.session.add(mongo)
#     db.session.add(mysql)
#     db.session.commit()



@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Skills))
        all_skills = list(result.scalars())
    return render_template("index.html", skills=all_skills)

if __name__ == '__main__':
    app.run(port=5003, debug=True)