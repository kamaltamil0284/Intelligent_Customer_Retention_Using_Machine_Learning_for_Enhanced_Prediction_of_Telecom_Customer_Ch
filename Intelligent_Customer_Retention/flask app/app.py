
from flask import Flask, render_template, request

from keras.models import load_model

app = Flask(__name__)
model = load_model("telcom_churn.h5")

@app.route('/')# rendering the html template
def home():
    return render_template('home.html')

@app.route('/')
def helloworld():
    return render_template('index.html')

@app.route('/assesment')
def prediction():
    return render_template('submit.html')


@app.route('/predict', methods=['post'])
def admin():
    a = request.form["customerid"]
    b = request.form["surname"]
    c = request.form["gender"]
    if (c == 'f'):
        c = 0
    if (c == 'm'):
        c = 1
    d = request.form["age"]

    t = [[int(a), int(b), int(c), int(d)]]
    print(t)
    x = model.predict(t)
    print(x[0])
    return render_template(x)

if __name__ == "__main__":
    app.run(debug=True)