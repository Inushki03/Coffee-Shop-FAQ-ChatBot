from flask import Flask,render_template,request,jsonify
from fuzzywuzzy import process
import json

app=Flask(__name__)

with open("faqs.json") as f:
    faqs=json.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get",methods=["POST"])
def chatboat_response():
    user_message= request.json.get("message", "").lower()
    best_match,score = process.extractOne(user_message,faqs.keys())

    if score>=60:
        bot_reply=faqs[best_match]
    else:
        bot_reply="Sorry, I can't answer it "
    
    return jsonify({"reply":bot_reply})


if __name__=="__main__":
    app.run(debug=True)
