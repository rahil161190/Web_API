
#Use the Python 3.13 Slim image as the base
FROM python:3.13-slim
#Set the working directory in the container
WORKDIR /flask-docker
#Copy the current directory content into the container's /app directory
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
#Install the required libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#Run the Flask application
CMD ["python", "-m", "flask", "--app", "loan_status_predict", "run" ,"--host=0.0.0.0"]


#Commands for terminal
# how to create docker images ---> "docker build -t loan_app ."----> if any error is there check in docker container folder and run , there we can get the link if it
#is not working then change the terminal  ---> "docker run -p 8000:5000 -d loan_app"
# 1)docker build -t loan_app .
# 2) docker images
# 3) docker run -d loan_app  , after this command go to docker image section and a link will be generate
# if that link is not openable try to change the link in terminal of pycharm "docker run -p 8000:5000 -d loan_app"
# Here loan_app is the name given