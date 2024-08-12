from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector
import os
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="vijwal",
    password="root123",
    database="medscan"
)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['xray']
        type = request.form['type']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))

            cursor = db.cursor()
            cursor.execute("SELECT info FROM Classifications WHERE type=%s", (type,))
            result = cursor.fetchone()

            if result:
                return render_template('result.html', result=result[0])
            else:
                flash('No classification information found for the selected type.', 'error')
                return redirect(url_for('main.upload'))
    return render_template('upload.html')

@main.route('/test_db')
def test_db():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        return f"Connected to database: {db_name[0]}"
    except Exception as e:
        return str(e)

@main.route('/result')
def result():
    return render_template('result.html')
