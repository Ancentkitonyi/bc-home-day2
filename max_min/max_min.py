def find_max_min(lisT):
    #Returns list containing [min, max]
    #If elements are equal return first element
   
    lisT.sort()
    if lisT[0] != lisT[-1]:
        return [lisT[0], lisT[-1]]
    elif lisT[0] == lisT[-1]:
        return [lisT[0]]
print find_max_min([3,5,7,1,2,9,6])
