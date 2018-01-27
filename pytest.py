from functScript import *
from nonfunctScript import *

def test_hello():
    assert hello("travis") == "Hello travis"

def test_goodbye():
    assert goodbye("travis") == "Goodbye travis"

    
test_hello()
test_goodbye()
