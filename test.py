import addtest #This imports the python function as a module that you can access

def test_add(): #Function to complete a test
    assert addtest.add(1,1) == 2 #This will take the function add within addtest.py and plugin a=1, b=1 and see if it is equal to 2.
                                 #The assert command will run the function and throw an error if the function does NOT return 1+1=2
