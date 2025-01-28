"""
data = "20-50-36-15-28
result = "21-51-37-16-29"
"""

def incrementString(s):
    output = ""
    new_str = s.split("-")
    update = [str(int(n)+1) for n in new_str]
    #output = [str(i)+'-' for i in update]
    res = "-".join(update)
    # for i in update:
    #     output = output+str(i)+'-'
    return res
j


if __name__ =='__main__':
    input_str = input("Enter the string separated by - : ")
    result = incrementString(input_str)
    print(result)