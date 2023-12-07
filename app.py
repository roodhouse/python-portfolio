from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# generate requirements.txt
# prepare server on AWS
# move publish and move site

load_dotenv()

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

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    demo = db.Column(db.String(250), nullable=False)
    code = db.Column(db.String(250), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    message = db.Column(db.String(1000), nullable=False)

class Social(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), nullable=False)
    bg_color = db.Column(db.String(250), nullable=False)

class NewContactForm(FlaskForm):
    name = StringField('', validators=[DataRequired()], render_kw={'placeholder': 'Name'})
    email = EmailField('', validators=[DataRequired()], render_kw={'placeholder': 'Email'})
    message = TextAreaField('', validators=[DataRequired()], render_kw={'rows': 10, 'placeholder': 'Message'})
    submit = SubmitField('Let\'s Collaborate')

with app.app_context():
    db.create_all()
    db.session.commit

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

# # # work seed
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

# # # project seed
# connect_four = Project(
#     title = 'Connect Four',
#     img_url = 'static/images/project/connectFour.png',
#     demo = 'https://connect.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-connect-four'
# )
# tic = Project(
#     title = 'Tic Tack Toe',
#     img_url = 'static/images/project/tic.png',
#     demo = 'https://tic.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-tic-tac-toe'
# )
# comments = Project(
#     title = 'Comments',
#     img_url = 'static/images/project/comments.png',
#     demo = 'https://comments.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-comments'
# )

# clock = Project(
#     title = 'Clock',
#     img_url = 'static/images/project/clock.png',
#     demo = 'https://clock.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-clock'
# )
# dictionary = Project(
#     title = 'Dictionary',
#     img_url = 'static/images/project/dictionary.png',
#     demo = 'https://dictionary.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-dictionary'
# )
# calc = Project(
#     title = 'Calculator',
#     img_url = 'static/images/project/calc.png',
#     demo = 'https://calc.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-calculator'
# )
# countdown = Project(
#     title = 'Countdown',
#     img_url = 'static/images/project/countdown.png',
#     demo = 'https://countdown.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-launch-countdown'
# )
# credit = Project(
#     title = 'Interactive CC',
#     img_url = 'static/images/project/credit.png',
#     demo = 'https://credit.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-interactive-card'
# )
# age = Project(
#     title = 'Age Calculator',
#     img_url = 'static/images/project/age.png',
#     demo = 'https://age.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-age-calc'
# )
# bmi = Project(
#     title = 'BMI Calculator',
#     img_url = 'static/images/project/bmi.png',
#     demo = 'https://bmi.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-bmi'
# )
# intro = Project(
#     title = 'Intro Landing',
#     img_url = 'static/images/project/intro.png',
#     demo = 'https://intro.rugh.us/',
#     code = 'https://github.com/roodhouse/new-frontend-mentor-intro-project'
# )
# soon = Project(
#     title = 'Coming Soon',
#     img_url = 'static/images/project/base.png',
#     demo = 'https://base-apparel.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-base-apparel'
# )
# pod = Project(
#     title = 'Pod Request',
#     img_url = 'static/images/project/request.png',
#     demo = 'https://request.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-pod-request-access'
# )
# skilled = Project(
#     title = 'Skilled',
#     img_url = 'static/images/project/skilled.png',
#     demo = 'https://skilled.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-skilled-landing-page'
# )
# work_it = Project(
#     title = 'Work It',
#     img_url = 'static/images/project/workit.png',
#     demo = 'https://workit.rugh.us/',
#     code = 'https://github.com/roodhouse/frontend-mentor-workit-landing-page'
# )

# # # social seed

# linkedin = Social(
#     name = 'LinkedIn',
#     img_url = 'static/images/social/linkedin.svg',
#     link = 'https://www.linkedin.com/in/john-m-rugh/',
#     bg_color = '#2563EB'
# )

# github = Social(
#     name = 'Github',
#     img_url = 'static/images/social/github.svg',
#     link = 'https://github.com/roodhouse',
#     bg_color = '#333333'
# )

# email = Social(
#     name = 'Email',
#     img_url = 'static/images/social/email.svg',
#     link = 'mailto: rughjm@gmail.com',
#     bg_color = '#6fc2b0'
# )

# resume = Social(
#     name = 'Resume',
#     img_url = 'static/images/social/resume.svg',
#     link = 'https://drive.google.com/file/d/139Km3FZpDCBKM2_d1czCcPPaT94pHVwG/view?usp=sharing',
#     bg_color = '#565f69'
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

#     db.session.add(connect_four)
#     db.session.add(tic)
#     db.session.add(comments)
#     db.session.add(clock)
#     db.session.add(dictionary)
#     db.session.add(calc)
#     db.session.add(countdown)
#     db.session.add(credit)
#     db.session.add(age)
#     db.session.add(bmi)
#     db.session.add(intro)
#     db.session.add(soon)
#     db.session.add(pod)
#     db.session.add(skilled)
#     db.session.add(work_it)
#     db.session.add(linkedin)
#     db.session.add(github)
#     db.session.add(email)
#     db.session.add(resume)

#     db.session.commit()

def send_email(name, message, email, to_email):
    print(email)
    email_acct = getenv('EMAIL')
    from_email = email
    password = getenv('PASSWORD')
    smtp_server = getenv('SERVER')
    port = getenv('PORT')
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to_email
    msg['Name'] = name
    msg['Subject'] = 'New comment from portfolio'
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(email_acct, password)
        server.sendmail(from_email, to_email, msg.as_string())

@app.route("/", methods=['GET', 'POST'])
def home():
    form = NewContactForm()
    if request.method == 'GET':
        with app.app_context():
            result = db.session.execute(db.select(Skills))
            work_result = db.session.execute(db.select(Work))
            project_result = db.session.execute(db.select(Project))
            social_result = db.session.execute(db.select(Social))
            all_skills = list(result.scalars())
            all_work = list(work_result.scalars())
            all_project = list(project_result.scalars())
            all_social = list(social_result.scalars())
        return render_template("index.html", skills=all_skills, work=all_work, project=all_project, social=all_social, form=form)
    else:
        if form.validate_on_submit():
            
            name = form.name.data
            email = form.email.data
            message = form.message.data

            new_contact = Contact(name=name, email=email, message=message)

            print(new_contact)

            try:
                send_email(name, message, email, 'rughjm@gmail.com')
                print(jsonify({'message': 'Email sent'}))
                
                with app.app_context():
                    try:
                        db.session.add(new_contact)
                        db.session.commit()
                        return redirect('/')
                    except Exception as e:
                        print('failure:', e)
                        db.session.rollback()

            except Exception as e:
                print(jsonify({'error': 'Failed to send email', 'details': str(e)}), 500)
                return redirect('/')

        else:
            return render_template("index.html", skills=all_skills, work=all_work, project=all_project, form=form)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(port=5003, debug=True)