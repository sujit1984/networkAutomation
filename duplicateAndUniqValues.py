"""
alst =["blr","chn", "mum", "tpuram", "blr", "blr", "chn", "hyd","blr"]

Expected:
unique_values=["mum", "tpuram", "hyd"]
duplicates =["blr","chn"]

"""
from collections import Counter

def uniqAndDuplicates(lst):
    unique_values =[]
    duplicates = []

    unique_values = [elem for elem in lst if lst.count(elem)==1]
    duplicates = {elem for elem in lst if lst.count(elem)!=1 }
    # counter = Counter(lst)
    # for item in lst:
    #     if counter[item]==1:
    #         unique_values.append(item)
    #     else:
    #         duplicates.append(item)
    #
    return unique_values,list(duplicates)

if __name__=='__main__':
    alst = ["blr","chn", "mum", "tpuram", "blr", "blr", "chn", "hyd","blr"]
    uniq,dup = uniqAndDuplicates(alst)
    print("unique_values =",uniq)
    print("duplicates =", dup)