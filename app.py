from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=["POST"])
def page_login():
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('userpassword')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
