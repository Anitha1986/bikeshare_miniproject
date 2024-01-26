import os,sys
sys.path.insert(0,os.getcwd())

from script import addition

def test_add():
    subj=addition(7,9)
    assert subj==16
    print("done")
    
test_add()