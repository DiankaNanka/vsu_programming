from itertools import permutations



def repl_num(a):
    a_n = int(a)


    all_num = []
    all_num_n = []


    for i in permutations(a,len(a)):
        all_num.append(''.join(i))

    for nm in all_num:
        all_num_n.append(int(nm))  
         
    all_num_n.sort() 

    i = len(all_num_n)-1

    while i <= len(all_num_n)-1:
        if all_num_n[i] == a_n:
            if i == len(all_num_n)-1:
                return -1
            else:
                return all_num_n[i+1]        
        i=i-1


a = input()
print(repl_num(a))

