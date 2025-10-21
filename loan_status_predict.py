import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from flask import Flask, request,jsonify
import pickle

app = Flask(__name__)

#Reading and saving the model
model_pickle = open('classifier.pkl', 'rb')
clf = pickle.load(model_pickle)

@app.route('/')
def hello_ping():
    return 'Hi welcome to Loan Status Prediction'
@app.route('/predict', methods=['POST'])
def prediction():
    loan_req = request.get_json()
    print("Received JSON:", loan_req)

    gender = 0 if loan_req['Gender'] == "Male" else 1
    married = 1 if loan_req['Married'] == "Yes" else 0
    dependents_map = {'0': 0, '1': 1, '2': 2, '3+': 3}
    dependents = dependents_map.get(loan_req['Dependents'], 0)
    education = 0 if loan_req['Education'] == "Not Graduate" else 1
    self_employed = 1 if loan_req['Self_Employed'] == "Yes" else 0
    credit_history = 1 if loan_req['Credit_History'] == "Yes" else 0

    applicant_income = float(loan_req['ApplicantIncome'])
    coapplicant_income = float(loan_req['CoapplicantIncome'])
    loan_amount = float(loan_req['LoanAmount'])

    input_vector = [[gender, married, dependents, education, self_employed,
                     applicant_income, coapplicant_income, loan_amount, credit_history]]

    result = clf.predict(input_vector)
    print("Prediction result:", result)

    return jsonify({"Loan_approval_status": int(result[0])})
if __name__ == '__main__':
    app.run(debug=True)


# Postman body
#{
  #"Gender": "Male",
  #"Married": "Yes",
  #"Dependents": "2",
  #"Education": "Not Graduate",
  #"Self_Employed": "No",
  #"ApplicantIncome": 5000,
  #"CoapplicantIncome": 2000,
  #"LoanAmount": 150,
  #"Credit_History": "No"
#}
