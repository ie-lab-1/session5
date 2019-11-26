### Deploying an Spyne application in AWS: An end-to-end tutorial

It's a simple Spyne app that serves a SOAP web service

To tool around with the app directly, here's a quickstart guide. 

Clone this repo to your local machine. In the top level directory, create a virtual environment:
```
$ virtualenv spyne-aws
$ source spyne-aws/bin/activate
```
Now install the required modules:
```
$ pip install -r requirements.txt
```
Now you can launch the app:
```
$ python application.py
```
And point your browser to http://localhost:8000/?wsdl
