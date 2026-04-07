import os
from flask import Flask, request, render_template

app = Flask(__name__)

otc_data = {
    "headache": {"drug": "paracetamol", "dose": "500mg every 4-6 hours"},
    "fever": {"drug": "ibuprofen", "dose": "200mg every 6-8 hours with food"},
    "cough": {"drug": "dextromethorphan", "dose": "10-20mg every 4 hours"},
    "heartburn": {"drug": "omeprazole", "dose": "20mg once daily before eating"},
    "allergy": {"drug": "cetirizine", "dose": "10mg once daily"}
}
#the first homepage you will see now is connecting to index file#
@app.route("/")
def home():
    return render_template("index.html")
########################################################################
"""
next page is the area user enter the symptom the request the argus
"""
@app.route("/check")
def check():
    symptom = request.args.get("symptom", " ").lower()
    if symptom in otc_data:
        result = otc_data[symptom]
        return f"Symptom: {symptom} = Drug: {result['drug']} | Dose: {result['dose']}"
    else:
        return f"Sorry, no OTC drug found for: {symptom}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
