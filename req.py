"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-two
http://stackoverflow.com/questions/14015592/how-to-create-a-new-unknown-or-dynamic-expando-object-in-python
http://stackoverflow.com/questions/2827623/python-create-object-and-add-attributes-to-it
"""

import requests

def get_example():
    r = requests.get('http://example.com/')
    print(dir(r))
    return r.status_code == 200

def get_example_no_call_req():
    r = lambda:None # forma de definir un objeto dinamico
    r.status_code = 200
    return r.status_code == 200

if __name__ == '__main__':
    print(get_example())
    print(get_example_no_call_req())
