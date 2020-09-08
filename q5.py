def has_33(lst):
     result=false
     for i in range(len(lst)-1):
         if lst[i] == 3 and lst[i+1] == 3:
             result=true
             return result

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))
