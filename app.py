#this code make our func clear and separate from + and - marks that is the most basic thing
def made_func_clear(func):
    """
    input  : function from the user (str) , this is may be messful and wanna upgrade. This helps
             program to understand function.
    return : upgraded function to drivative machine

    """
    tempL = list(func)
    for index in range(0,len(tempL)):
        p = tempL[index]
        if p == '-' and not index==0:
            tempL[index-1] += '+'

    func = ''.join(''.join(tempL).split()).split('+')

    temp_func_list = []
    
    for i in range(len(func)):

        switch = False
        temp_func = ''
        pwr ='0'
        count = 0

        #print(f'++++++++++++ Im i and im in {func[i]}')

        for p in range(len(func[i])):

            #print(f' ------------- Im p and im in {func[i][p]}')

            if func[i][p].isdigit() and not switch or func[i][p] == '-':
                temp_func+=func[i][p]
                #print(f'Updated Temp func -------> {temp_func}')
    
            elif func[i][p] in 'x':
                switch = True

            if switch:
                if func[i][p].isdigit():
                    if pwr == '0':
                        pwr = func[i][p]
                    else:
                        pwr += func[i][p]
                    count = int(pwr)
                elif func[i][p] == 'x':
                    count+=1

        if count!=0:
            pwr = str(count)

                
        temp_func+='*x^'+pwr+'^'
        #print(f'Updated Temp func -------> {temp_func}')
        temp_func_list.append(temp_func)
        #print(f'i loop doneeeeee +++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    print(temp_func_list)
    return temp_func_list


#drivative macine
def drivative(func):
    upgraded_func = ''.join(made_func_clear(func)).split('^')
    upgraded_func.pop()
    print(f'\nThis is the function nedd to work with : {upgraded_func}\n')

    """for index in range(len(upgraded_func)):
        DyDx = ''
        part = upgraded_func[index]
        for vice_index in range(len(part)):
            if part[vice_index] == '*':
                for n in range(vice_index +3,len(part)):
                    DyDx += '*'+part[n]
                    print(f'Updated DyDx * : {DyDx}\n{vice_index}')

            else:
                if part[vice_index] == '^':
                    print('found')
                    temp = '0'
                    for p in range(vice_index+1,len(part)):
                        if not p == len(part):
                            if temp == '0':
                                temp=part[p]
                            else:
                                temp+=part[p]
                            print(f'adiing temp : {temp}')

                        DyDx += str(int(temp)-1)
                        print(f'Updated DyDx - : {DyDx}')
                DyDx+=part[vice_index]
                print(f'Updated DyDx : {DyDx}\n{vice_index}')"""

    #we need to run for loops one by one and drivatate the functions one by one









func = input('What is the function : ').replace("^","").lower()
drivative(func)