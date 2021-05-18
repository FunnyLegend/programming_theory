argsize=2
F=['T(1,2)','T(0,1)','Z(0)','J(1,4,0)','J(2,3,9)','S(3)','S(0)','J(0,0,5)','S(4)','Z(3)','J(0,0,4)']
g1=['T(1,2)','T(0,1)','Z(0)','J(1,4,0)','J(2,3,9)','S(3)','S(0)','J(0,0,5)','S(4)','Z(3)','J(0,0,4)']
g2=['J(0,2,5)','J(1,2,0)','S(2)','J(0,0,1)','T(1,0)']
prog=[F,g1,g2]
max_reg=[]
#looking for maximum number of register
for i in range(0,len(prog)):
    reg=[]
    for j in range(0,len(prog[i])):
        if prog[i][j][0]=='Z'or prog[i][j][0]=='S':
            reg.append(int(prog[i][j][-2]))
        if prog[i][j][0]=='T':
            reg.append(int(prog[i][j][-2]))
            reg.append(int(prog[i][j][2]))

        if j==len(prog[i])-1:
            max_reg.append(max(reg))
#adresses for programs start registers
first_reg=[0]

for i in range(1,len(prog)):
    first_reg.append(first_reg[i-1]+max_reg[i-1]+1)
cur_comsize=(argsize+1)*(len(prog)-1)
#move programs registers to their intervals
for i in range(1,len(prog)):
        for j in range(0,len(prog[i])):
            temp=prog[i][j][2:-1].split(',')
            temp[0]=int(temp[0])+int(first_reg[i]);
                 
            if prog[i][j][0]=='Z'or prog[i][j][0]=='S':              
                prog[i][j]=prog[i][j][:2] + str(temp[0])+prog[i][j][-1]               
            if prog[i][j][0]=='T':
                temp[1]=int(temp[1])+int(first_reg[i]);
                prog[i][j]=prog[i][j][:2] + str(temp[0])+','+str(temp[1])+prog[i][j][-1]
            if prog[i][j][0]=='J':
                temp[1]=int(temp[1])+int(first_reg[i]);
                if  int(prog[i][j][-2])==0 or int(prog[i][j][-2])>len(prog[i]):
                    temp[2]=cur_comsize+len(prog[i])+1               
                    prog[i][j]=prog[i][j][:2] + str(temp[0])+','+str(temp[1])+','+str(temp[2])+prog[i][j][-1]
                else:
                     temp[2]=int(temp[2])+cur_comsize 
                     
                     prog[i][j]=prog[i][j][:2] + str(temp[0])+','+str(temp[1])+','+str(temp[2])+prog[i][j][-1]
                     

        cur_comsize+=len(prog[i])  

# Making T operations for moving resulting data
finalMove = []
for i in range(1, len(prog)):
    finalMove += ["T("+ str(first_reg[i]) + "," + str(i) + ")"]


cur_comsize += len(prog) - 1
#Changing f program J operation registers
for i in range(0,len(prog[0])):
    if prog[0][i][0]=='J':
         temp=prog[0][i][2:-1].split(',')
         if int(temp[2])> len(prog[0]):
             temp[2]=0;
             
         elif int(temp[2])!=0:
             temp[2]=int(temp[2])+cur_comsize
         prog[0][i]= prog[0][i][:6]+str(temp[2])+ prog[0][i][-1]


#making T operations to move input data
T=[]
for i in range(1, len(prog)):
     for j in range(0,argsize+1):
        T.append('T('+str(j)+','+str(first_reg[i]+j)+')')

result=T


for i in range(1,len(prog)):
    result+=prog[i]
result+=finalMove
result+=prog[0]
for i in range(0,len(result)):
    print(result[i],'\n')