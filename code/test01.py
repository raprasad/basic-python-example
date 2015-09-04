from os.path import isfile
#import pandas as pd
from test02 import print_goodbye 
 
def print_apple(apple='red'):
    print apple
     
def print_hello(**kwargs):
    print 'hello' 
    print kwargs.get('apple', 'nuthin')
    fname = '../data/fearonlaitin.tab'
    print_goodbye()



    # data file
    #fname = '../data/fearonlaitin.tab'

if __name__=='__main__':
    print_apple()
    #print_hello(apple='green')