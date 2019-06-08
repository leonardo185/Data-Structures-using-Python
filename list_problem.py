#DSA-Assgn-1
def merge_list(list1, list2):
    list2.reverse()
    resultant_data = []
    for i in range(len(list1)):
        if(list1[i] != None and list2[i] != None):
            resultant_data.append(list1[i] + list2[i])
        elif(list1[i] != None and list2[i] == None):
            resultant_data.append(list1[i])
        elif(list1[i] == None and list2[i] != None):
            resultant_data.append(list2[i])
        else:
            continue
    #write your logic here
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(*merged_data)
