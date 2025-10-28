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
    return 'Hi welcome to Loan Status Prediction model version 2 !'

@app.route("/ping")
def  pinger():
    return 'Hi I am a pinger'
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
#Loan_prediction(Rahil)  ---> is the ipynb file from pickle file is created

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

# steps for ecr repo with docker images and github actions
#First of all activate your enviornment in the terminal with command " .\venv\Scripts\activate",here it is venv .
# 1)find credentials of aws
# 2) set the default region to virginia Us east at aws website
# 3) get the access keys (search IAM --> user> create access keys) and store secretly
# 3) make ecr repo with a name (ex:- loan_app)
# 4) install awsCLI into the system using commands
# 4a) --> & "C:\Program Files\Amazon\AWSCLIV2\aws.exe" configure     (copy whole tex)
# 4b) write access id and access key in the terminal and enter two times
# if the above region was set to none or something else then write in terminal  "& "C:\Program Files\Amazon\AWSCLIV2\aws.exe" configure set region us-east-1"
# 5) (optional)check how many docker images are set using "docker images"
# 6) connect docker with awscli using command (check view push command and copy paste those command for windows "C:\Program Files\Amazon\AWSCLIV2\aws.exe" use ahead of get login command)--> " & "C:\Program Files\Amazon\AWSCLIV2\aws.exe" ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 495599778234.dkr.ecr.us-east-1.amazonaws.com"
#7)  image creation at docker  "docker build --platform=linux/amd64 -t loan_app ."
#8) "docker tag loan_app:latest 495599778234.dkr.ecr.us-east-1.amazonaws.com/loan_app:latest"-->(this command will push image to ECR)
# 9) images are set at ecr(multiple meta copies might be there but "latest" is the only one to use) , copy the image URI--
# 10) Search ECS ---> create cluster with name ex:- loan-app-cluster" -- >task definitions --> task_definition name like ex: flask_task --> select aws fargate -->paste the image URI ---> rest keep as it is default --->create ---> run task --->networking section choose security group
# in that 1st is http with port range 80 and and source is anywhere ,2nd is custom TCP where port range is 5000 and source is anywhere
# 11) task should be runnning, go inside and see public ip address
# 12) now go to this urlink and copy the code https://github.com/aws-actions/amazon-ecs-deploy-task-definition
#13) now follow rest of command on yaml documents continue....
