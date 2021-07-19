def numbers(num):
    count = 0
    for one in range(1,num):
        for two in range(num,0,-1):
            if one == two:
                break
            if one + two == num:
                count+=1
    print(count)

numbers(int(input()))
