from flask import Flask,render_template,url_for,get_flashed_messages,flash,redirect
from wtforms import StringField,EmailField,TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,Length
from bleach import clean
from html import escape
from flask_wtf import CSRFProtect
import smtplib
from markupsafe import escape
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app = Flask(__name__)
app.config["SECRET_KEY"] = "Ye@#212dasjkdj321EJWJDLJJDS2312LJDsdhakjhsaKJHkhkjhhhKH^UT67IYYuhyg*yiuhyYigUG(hig(9))"
csrf = CSRFProtect(app)


class Contact(FlaskForm):
    name = StringField("Full Name",validators=[DataRequired("Name is Required"),Length(min=5,max=50,message="Name must be between 5 - 10")])
    email = EmailField("Email",validators=[DataRequired("Email is required"),Length(min=10,max=50,message='Email must be between 10 -50')])
    message = TextAreaField("Message", validators=[DataRequired("Message is require"),Length(min=50,max=500,message="Message must be between 5 - 500")])

    
@app.route("/")
def home():
    return render_template("index.html", show=True)

@app.route("/contact",methods=["POST","GET"])
def contact():
    form = Contact()
    if form.validate_on_submit():
        name = clean(escape(form.name.data))
        email = clean(escape(form.email.data))
        messages = clean(escape(form.message.data))
        passw = "jvqo ohff thol ovay"
        from_user = "yeabsiratesfaye4118@gmail.com"
        to_user = "yeabsiratesfaye4118@gmail.com"
        subject = "Your Portfolio Contact "
        message = MIMEMultipart()
        message["From"] = from_user
        message["To"] = to_user
        message["Subject"] = subject
        body = f"-name: {name}\n-email: {email}\n-message: {messages}"
        message.attach(MIMEText(body, "plain"))
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  
                server.login(from_user, passw)  
                server.send_message(message)  
                flash("Successfully send","success")
                return redirect(url_for('home'))
        except Exception as e:
            flash(f"An error occurred","error")

    return render_template("contact.html", form=form ,show=False)

@app.route("/git_hotel", methods=["POST","GET"])
def git_hotel():
    return redirect("https://github.com/Yeabsiraty/Hotel-Php-Website")

@app.route("/git_java", methods=["POST","GET"])
def git_java():
    return redirect("https://github.com/Yeabsiraty/Java-group-work-GUI")

@app.route("/git_python", methods=["POST","GET"])
def git_python():
    return redirect("https://github.com/Yeabsiraty/Python-projects")

if __name__ == "__main__":
    app.run(debug=True)