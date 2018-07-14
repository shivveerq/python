from sys import argv
args=argv[1:]# Read command line argument from starting to end
sum=0 # Declare sum object
for x in args :n=int(x) # this is for loop 
sum=sum+n # sum of command kine argument
print("sum of command line argument",sum) # orint command line argument
print("args",argv[1:2]) # print command line argument from 1 to 2 position