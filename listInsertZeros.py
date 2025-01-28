"""
Given:
numlst = [1,2,3,4,5]
Expected:
newlst=[1,0,2,0,3,0,4,0,5,0]
"""

def insertZeros(lst):
    newlist = []
    #output = [newlist.append(item), newlist.append(0) for item in lst]
    for item in lst:
        newlist.append(item)
        newlist.append(0)
    return newlist

if __name__=='__main__':
    input_list =[1,2,3,4,5]
    result = insertZeros(input_list)
    print(result)