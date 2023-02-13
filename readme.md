## Todo App and The AWS Code Family

### Project Overview

This is a simple web app set up with Flask. It allows the creation and deletion of tasks, like a Todo List.
The goal of the project is to use the AWS Code Family to build and deploy this application to a computing resource such as Amazon EC2 or Amazon Elastic Beanstalk.
The other main goal is to set up automation with CI/CD using AWS CodePipeline as part of the DevOps workflow.

### File structure
* `app.py` - main file with the todos
* `run.py` - sets up the application entry point and runs the Flask app.
* `requirements.txt` - lists the dependencies for the application.
* `/templates/*.html` - content pages
* `/static/style.css` - stylesheet for the application
* `buildspec.yml` - config file to be used by AWS CodeBuild

### Dependencies
* AWS Code Family
    * CodeCommit
    * CodeBuild
    * CodeDeploy
    * CodePipeline
* AWS Cloud9 / Local IDE
* AWS CLI
* AWS EB CLI

To start the application, run the following command: (For Linux/Unix-based systems)
```
export FLASK_APP=run.py
flask run
```
Use the `set` command for Windows:
```
set FLASK_APP=run.py
flask run
```
You can also simply use `python app.py`.