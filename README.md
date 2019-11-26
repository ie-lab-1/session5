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

Now that the server implementation is done, you can run it. Now it’s time to actually make a request to our server to see it working.
You can test your service using suds. Suds is a separate project for implementing pure-python soap clients. To learn more visit the project’s page: https://fedorahosted.org/suds/. You can simply install it using easy_install suds.

So, here’s a three-line script that illustrates how you can use suds to test your new Spyne service:
```
from suds.client import Client
hello_client = Client('http://localhost:8000/?wsdl')
print hello_client.service.say_hello("Dave", 5)
```
The script’s output would be as follows:
```
(stringArray){
    string[] =
        "Hello, Dave",
        "Hello, Dave",
        "Hello, Dave",
        "Hello, Dave",
        "Hello, Dave",
    }
```
The corresponding response document would be:
```
<?xml version='1.0' encoding='UTF-8'?>
<senv:Envelope xmlns:tns="spyne.examples.hello.soap" xmlns:senv="http://schemas.xmlsoap.org/soap/envelope/">
  <senv:Body>
    <tns:say_helloResponse>
      <tns:say_helloResult>
        <tns:string>Hello, Dave</tns:string>
        <tns:string>Hello, Dave</tns:string>
        <tns:string>Hello, Dave</tns:string>
        <tns:string>Hello, Dave</tns:string>
        <tns:string>Hello, Dave</tns:string>
      </tns:say_helloResult>
    </tns:say_helloResponse>
  </senv:Body>
</senv:Envelope>
```
