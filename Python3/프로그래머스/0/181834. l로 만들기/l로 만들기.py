def solution(myString):
    tmp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    for i in tmp :
        myString = myString.replace(i, 'l')    
    return myString.replace(i, 'l')