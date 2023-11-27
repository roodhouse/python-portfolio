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

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    demo = db.Column(db.String(250), nullable=False)
    code = db.Column(db.String(250), nullable=False)

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

# entertainment = Work(
#     title = 'Full Stack Entertainment App',
#     img_url = 'static/images/work/entertainmentApp.png',
#     demo = 'https://entertainment.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-entertainment'
# )
# galleria = Work(
#     title = 'Art Gallery',
#     img_url = 'static/images/work/galleria.png',
#     demo = 'https://galleria.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-galleria'
# )
# space = Work(
#     title = 'Space Tourism',
#     img_url = 'static/images/work/space.png',
#     demo = 'https://space.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-space'
# )
# rd_blog = Work(
#     title = 'Rugh Design Blog',
#     img_url = 'static/images/work/color-review-new.png',
#     demo = 'https://rugh.design/review',
#     code = 'https://github.com/roodhouse/rugh-design-landing-page/tree/main/client/src/components/blog'
# )
# bucket = Work(
#     title = 'Bucket List Blog',
#     img_url = 'static/images/work/bucket_list.png',
#     demo = 'https://bucket-list-blog.herokuapp.com/',
#     code = 'https://github.com/roodhouse/project2-CRUD-Happens'
# )
# color_wheel = Work(
#     title = 'Color Wheel',
#     img_url = 'static/images/work/color-wheel-icon.svg',
#     demo = 'https://rugh.design/color-wheel/',
#     code = 'https://github.com/roodhouse/rugh-design-color-wheel'
# )
# rd_home = Work(
#     title = 'Rugh Design Homepage',
#     img_url = 'static/images/work/RDhome.png',
#     demo = 'https://rugh.design/',
#     code = 'https://github.com/roodhouse/rugh-design-landing-page'
# )
# ebook = Work(
#     title = 'eBook Landing Page',
#     img_url = 'static/images/work/paint_colors.png',
#     demo = 'https://www.rughdesign.com/own-your-space/',
#     code = 'https://www.rughdesign.com/own-your-space/'
# )
# review = Work(
#     title = 'Re:View',
#     img_url = 'static/images/work/review_blog.png',
#     demo = 'https://review-binary-beast.herokuapp.com/',
#     code = 'https://github.com/roodhouse/UPIN'
# )

# with app.app_context():
#     db.session.add(entertainment)
#     db.session.add(galleria)
#     db.session.add(space)
#     db.session.add(rd_blog)
#     db.session.add(bucket)
#     db.session.add(color_wheel)
#     db.session.add(rd_home)
#     db.session.add(ebook)
#     db.session.add(review)
#     db.session.commit()


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Skills))
        work_result = db.session.execute(db.select(Work))
        all_skills = list(result.scalars())
        all_work = list(work_result.scalars())
    return render_template("index.html", skills=all_skills, work=all_work)

if __name__ == '__main__':
    app.run(port=5003, debug=True)