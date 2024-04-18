## Flask Jumble API

The Flask Jumble API provides a simple service that jumbles words based on a given integer `1= <n =< 100`, which shifts each letter by `n` positions in the alphabet. This project is structured in a way that can be deployed effectively using Docker and heroku. A working backend has been created using Flask [Jumble Web API](https://japi-dd84663b4b52.herokuapp.com/) 

## Folder/File structure: 

This file structure is created in a way that can be used for modularity in the future. 

1. There are 2 files created inside the [App Folder](app). It is the main application directory for the service( services.py, routes.py ). The jumble function is created inside the services and Routes have been configured inside the routes

2. app.py initializes the Flask application. (Entry point)

3. For testing the services a separate folder is located at [Test Folder](tests). The test is divided into unit testing, API testing and, limiter testing.[Unit Test ](tests/test_unit.py) [API Test ](tests/test_api.py) [LIMITER Test ](tests/test_limiter.py)

4. A Dockerfile is created for building the container for deployment.

5. All the libraries are added inside requirements.txt

## MVP Features

- ```REST API to jumble words Q1 & Q2```: This is the main function of the api to shift/jumble the words when an int n is passed. The function is created inside the services.py. The services.py is being imported inside the routes. def api_jumble is responsible for handling the post method of the requested payload.
  
- ```Basic Landing page```: This is a further implementation of the def api_jumble where users would be able to see a landing page after starting the server and html page will be rendered for inputting a string and the desired shift amount. E.g 
Enter Text : <some-text> Shift Amount :<n>. After hitting the button jumble it!, users would be able to see the desire output and also come back to the previous page for inputing another message.

- ```Rate Limit on the API Q5```: A rate limiter has been added where users would not be able to make more 300 requests per minute. A limiter library has been used for configuration inside the route.py.

- ```Testing```: Unit testing, API testing has been done thoroughly but there might be some edge cases to consider. (Negative numbers for shifting, or shifting number more than 1000) 
  
- ```Jumble Container Q4```: A docker container has been created for deploying it on heroku. Further implementation details can be found inside the Dockerfile.

### Check [ApplicationScreenshot folder](Screenshots)

## Local setup and testing

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3.9.0
- pip (v - 24)
- virtualenv (optional)
- libraries are added inside the requirements.txt
- If not, use pip freeze requirements for checking the libraries used
  
- Install the dependencies:

```bash
 pip install -r requirements.txt
```
- To run the development server (from the root directory):
  
```bash
python app.py
```

- To run all the test files (unit testing, API testing, limiter testing) use the following command:

```bash
pytest
```

- To run a specific test file, use the following command:

```bash
pytest tests/<file-name> 
```
Replace file-name with test_unit.py, test_limiter.py, test_api.py

- Curl can be used in a bash terminal to test the /api/jumble/{n} :

- For single request test
  
```bash
curl -X POST http://localhost:5000/api/jumble/2 \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello World!"}'
```
```bash
Output: {
  "jumbled": "Jgnnq Yqtnf"
}
```

- Testing Rate Limiting for 300 requests per minute
- Run the following script inside the tests folder.
```bash
./test_api.sh
```

```bash
Output:
<html la<!doctype html>
<html lang=en>
<title>429 Too Many Requests</title>
<h1>Too Many Requests</h1>
<!doctype html>
<html la<!doctype html>
<html lang=en>
<title>429 Too Many Requests</title>
<h1>Too Many Requests</h1>
<p>300 per 1 minute</p>
```


- Postman can be used as well for the API testing.

```bash
Go to the Headers tab and ensure there is a header with Key as Content-Type and Value as application/json.

Under the Body tab, select raw and then choose JSON from the dropdown that adjusts the text input format. Postman usually automatically adds the correct Content-Type header when you select JSON as the body type.
```


## Deployment Guide (Docker)

The following instructions are provided for creating a container inside docker.

### Prerequisites
- install Docker
- Check the [Dockerfile](Dockerfile) for setting up the docker build.
- Build the image locally:
  
```bash
docker image build -t <my-app> .
```
NOTE: my-app can be any name for the image. Use bash terminal for running the commands as some commands might not work in a command promt or powershell

- Verify if the image has been created locally:

```bash
docker image ls
```
- Run the Docker Container:

```bash
docker run -p 5000:5000 -d <my-app>
```
Note: Replace <my-app>

## Deployment Guide (Heroku)

The following instructions are provided to deploy the docker container onto heroku.
  
### Prerequisites

- Sign up in heroku
    
- Login using bash terminal:

```bash
heroku container:login
```
It would open the browser and prompt you to log in with your Heroku credentials, just click Login on the new browser tab.

- Create the app on heroku:

```bash
heroku create <name-for-your-app>
```
Place jaas as your app name (japi in my case) or any name but follow the guideline. The guide will be shown in the promt

- Push the container:

```bash
heroku container:push web --app <name-for-your-app>
```
- Use the following command to deploy the container:

```bash
heroku container:release web --app <name-for-your-app>
```

- Open the app in the browser using the following command:
  
```bash
heroku open --app <name-for-your-app>
```
#### Check [Jumble Web API](https://japi-dd84663b4b52.herokuapp.com/)

### Built With
- Flask
- Flask-Limiter

### Next Steps for the Project
- A minor bug for the test file needs to be fixed where the limiter has not been initialized properly inside the 
  test_limiter.py. A bash [script](tests/test_api.sh) is created for testing the limiter.
- Setting up a front end using React and tailwind to provide a view.
- Automating the testing process using only one script.
- Working on the modularity of the code like refactoring.
- Depending on the services, a database can be integrated for storing user information.
- Deploying the application using EC2 aws.
- Using Docker-compose to reflect the changes directly when running the container.
- Integrating a CI/CD pipeline.
  
### Author
- Sheikh Rahman

