from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
model = pickle.load(open("model2.pkl","rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods= [ "GET","Post"])
def predict():
    input1 = float(request.form["input1"])
    input2 = float(request.form["input2"])
    input3 = float(request.form["input3"])
    input4 = float(request.form["input4"])
    input5 = float(request.form["input5"])
    input6 = float(request.form["input6"])
    input7 = float(request.form["input7"])
    result = model.predict([[input1,input2,input3,input4,input5,input6,input7]])
    return render_template("index.html",**locals)
if __name__ == "__main__":
    app.run(debug=True)