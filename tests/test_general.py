from deploy_test import Dummy

def test_dummy_init():
    Dummy('hello')

def test_print():
    d = Dummy('hello')
    d.dummy_func()