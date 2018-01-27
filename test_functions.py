from functScript import *
from nonfunctScript import *

def test_hello():
    assert hello("travis") == "hello travis"

def test_goodbye():
    assert goodbye("travis") == "Goodbye travis"
