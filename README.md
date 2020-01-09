# MeMD Diagnosis Map Microservice

MeMD is a mobile App that allows a user to self diagnosis medical conditions and find the closest specialists. After a user is given a diagnosis they receive an email with their results as well as a list of providers in their area who take the user's insurance, and a map of the US showing the distribution of MeMD users with the same diagnosis.

<img width="1050" alt="Screen Shot 2020-01-08 at 5 44 15 PM" src="https://user-images.githubusercontent.com/47466067/72028120-54998400-3279-11ea-961d-7e35b46cc4f4.png">

### Table of Contents

<!--ts-->
   * [Table of Contents](#table-of-contents)
   * [Set Up](#set-up)
   * [Focuses](#focuses)
   * [Tech Stack](#tech-stack)
<!--te-->


## **Set Up**

### Clone repo
```
https://github.com/me-md/memd-diagnosis-map-api
```
### Set up a virtual environment

Install **pip** first

    sudo apt-get install python3-pip

Then install **virtualenv** using pip3

    sudo pip3 install virtualenv

Now create a virtual environment

    virtualenv venv

>you can use any name insted of **venv**

You can also use a Python interpreter of your choice

    virtualenv -p /usr/bin/python2.7 venv

Active your virtual environment:

    source venv/bin/activate

To deactivate your virtual environment:

    deactivate


### Install dependencies
```
pip install -r requirements.txt
```
### Initalize Alembic
```
python manage.py db init
```
### Run Migrations
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Run the Server
```
Python app.py
```


### **Focuses**

The primary learning goals for this project are:

- Use an agile process to turn well defined requirements into deployed and production ready software
- Gain experience dividing applications into components and domains of responsibilities to facilitate multi-developer teams.
- Explore and implement new concepts, patterns, or libraries that have not been explicitly taught while at Turing
- Gain more experience using continuous integration tools to build and automate the deployment of features in various environments
- Build applications that execute in development, test, CI, and production environments
- Focus on communication between front-end and back-end teams in order to complete and deploy features that have been outlined by the project spec

### **Tech Stack**
- Python/Flask
- PostgeSQL
- Matplotlib
- Pandas
- Geopandas
