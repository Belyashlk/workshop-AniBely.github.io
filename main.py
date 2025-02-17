from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

def send_email(name, age, email, experience, motivation):
    sender_email = "catteam@internet.ru"
    sender_password = "G2hMyhVi0UeKtzFsZwbq"
    receiver_email = "fifa501@bk.ru"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Заявка на тестирование VisiGen"

    body = f"""
    ФИО: {name}
    Возраст: {age}
    Email: {email}
    Опыт работы с нейросетями: {experience}
    Мотивация: {motivation}
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.mail.ru', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            return "Письмо успешно отправлено!"
    except Exception as e:
        return f"Ошибка при отправке письма: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def handle_form():
    data = request.form
    name = data['name']
    age = data['age']
    email = data['email']
    experience = data['experience']
    motivation = data['motivation']
    
    result = send_email(name, age, email, experience, motivation)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
