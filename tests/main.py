from todo import main

def test_func1():
    r =  main.root()
    assert(r == "Hello World")

def test_func2():
    r = main.read_todo()
    assert r != "Pak"
