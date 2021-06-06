import os
from flask import Flask, request, render_template, redirect, url_for, make_response
from wtforms import Form, validators, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired # Need data before submit.
from flask_wtf import FlaskForm
# SQL Module Imports
import mysql.connector
# Connect MySQL
maxdb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL!@#2021Test",
)
cursor = maxdb.cursor()

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

class LoginForm(FlaskForm):
    name = StringField("Useername",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Submit")

class TableForm(FlaskForm):
    src_ip = StringField("Source IP",validators=[DataRequired()])
    time = StringField("Source IP",validators=[DataRequired()])
    FQDN = StringField("Source IP",validators=[DataRequired()])
    submit = SubmitField('Submit')

# Home page
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_info = LoginForm()
    if request.method == 'POST' and login_info.validate_on_submit():
        name = request.form["name"]
        password = request.form["password"]
        if name == "joy@gmail.com" and password == "password":
            return render_template("login.html", login_info=login_info)
        else:
            return redirect(url_for("index"))
    return render_template("login.html", login_info=login_info)

@app.route('/table', methods=['GET', 'POST'])
def table():
    table_info = TableForm()
    if request.method == 'POST' and table_info.validate_on_submit():
        src_ip = request.form["src_ip"]
        start_time = request.form["start_time"]
        end_time = request.form["end_time"]
        FQDN = request.form["FQDN"]
        # Use database = "DB_FullStackTest"
        cursor.execute("use DB_FullStackTest")
        sql_cmd = f"""
        SELECT Date,
            Time,
            usec,
            SourceIP,
            SourcePort,
            DestinationIP,
            DestinationPort,
            FQDN
        FROM  Table_FullStackTest
        WHERE (SourceIP={src_ip})
        AND (Date BETWEEN {start_time} AND {end_time})
        AND (FQDN={FQDN})
        ORDER BY Date, Time, usec ASC
        """
        cursor.execute(sql_cmd)
        content = cursor.fetchall()
        # columns name
        sql_col = "SHOW FIELDS FROM Table_FullStackTest"
        cursor.execute(sql_col)
        labels = cursor.fetchall()
        labels = [l[0] for l in labels]
    return render_template("table.html", table_info=table_info, labels=labels, content=content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5432))
    app.run(host='0.0.0.0', port=port, debug=True)