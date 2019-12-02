from suds.client import Client as SudsClient

url = 'http://ec2-3-10-56-239.eu-west-2.compute.amazonaws.com/soap/someservice?wsdl'
client = SudsClient(url=url, cache=None)
r = client.service.echo(str='hello world', cnt=3)
print (r)
