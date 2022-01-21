
def func1(intvar,floatvar,stringvar,charvar,listvar,tuplevar,setvar,dict):
        print(f"variables of func2:{intvar}{floatvar}{stringvar}{charvar}{listvar}{tuplevar}{setvar}{dict}",end="\n")

def func2(list):
        print(f"variables of func2:{list}")

def func3(no1,no2):
        print(f"variables of func3-- no1 :{no1} no2 :{no2}")

if __name__ == "__main__" :
    list1=[1,2,3]
    TUPLE1=(4,5,6)
    dict={'a:apple','b:ball','c:cat'}
    thisset = {"apple", "banana", "cherry"}
    func1(10,10.2,"Shivani",'a',list1,TUPLE1,thisset,dict)
    func2(['p','q','r'])
    func3(10,20)
