from funcScript import *
from nonfunctScript import *

def test_hello():
    assert hello("travis") == "Hello travis"

def test_goodbye():
    assert goodbye("travis") == "Goodbye travis"
