from flask import Flask,request,render_template
import pickle
import smtplib

app = Flask(__name__)

people = []

@app.route('/')
def getvalue():
    return render_template('task.html')

@app.route('/', methods=["POST"])
def form():
        nam = request.form.get("name")
        con = request.form.get("contact")
        em = request.form.get("email")
        mess = request.form.get("message") 
        pop = "You have successfully sent it"

        server= smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("tulikasinha7865@gmail.com","Sinha@08#")
        server.sendmail("tulikasinha7865@gmail.com",em,pop)

        if not nam or not con or not em or not mess:
            error ="All form fields required"   
        return render_template("home.html",n=nam,  num=con ,  e=em, mes = mess, err=error)



if __name__ == '__main__':
    app.run(debug=True)