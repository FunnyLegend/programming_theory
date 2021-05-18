prog=['T(1,2)','T(0,1)','Z(0)','J(1,4,0)','J(2,3,9)','S(3)','S(0)','J(0,0,5)','S(4)','Z(3)','J(0,0,4)']

argsize=2
startRegister = argsize + 3

result = []
T = []
for i in range(0, argsize+2):
        T += ["T("+ str(i) + "," + str(startRegister+i) + ")"]
  
result += T
for i in range(0,len(prog)):
    temp=prog[i][2:-1].split(',')
    temp[0]=int(temp[0])+startRegister
    if prog[i][0]=='Z'or prog[i][0]=='S':              
        prog[i]=prog[i][:2] + str(temp[0])+prog[i][-1]               
    if prog[i][0]=='T':
        temp[1]=int(temp[1])+startRegister
        prog[i]=prog[i][:2] + str(temp[0])+','+str(temp[1])+prog[i][-1]
    if prog[i][0]=='J':
        temp[1]=int(temp[1])+startRegister
        if  int(prog[i][-2])==0 or int(prog[i][-2])>len(prog[i]):
            temp[2]=len(T)+len(prog[i])+1  
            prog[i]=prog[i][:2] + str(temp[0])+','+str(temp[1])+','+str(temp[2])+prog[i][-1]
        else:
            temp[2]=int(temp[2])+len(T)
                     
            prog[i]=prog[i][:2] + str(temp[0])+','+str(temp[1])+','+str(temp[2])+prog[i][-1]
                     

      
result+=prog
result += [f"J({argsize+2},{startRegister}," + \
                                       f"{len(T) + len(prog)+4})"]
result+=[f"S({argsize+1})"]
result+=["J(0,0,1)"]
result+=[f"T({argsize+1},0)"]
for i in range(0,len(result)):
    print(result[i],'\n')