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
And point your browser to http://localhost:80/soap/someservice?wsdl

Now that the server implementation is done, you can run it. Now it’s time to actually make a request to our server to see it working.
You can test your service using suds. Suds is a separate project for implementing pure-python soap clients. To learn more visit the project’s page: https://fedorahosted.org/suds/. You can simply install it with the command install suds.

```
$ pip install suds-py3
```

So, here’s a three-line script that illustrates how you can use suds to test your new Spyne service:
```
from suds.client import Client as SudsClient

#url = 'http://ec2-3-10-56-239.eu-west-2.compute.amazonaws.com/soap/someservice?wsdl'
url = 'http://127.0.0.1:80/soap/someservice?wsdl'
client = SudsClient(url=url, cache=None)
r = client.service.echo(str='hello world', cnt=3)
print r
```
That can be run using the file client.py, using the right url: local or remote aws
```
$ python client.py
```
