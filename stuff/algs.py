def binarySearchStr(tocheck , list , param1 , param2 , pointer):
    if tocheck[pointer] < list[(param1 + param2)// 2]:
        binarySearchStr(tocheck , list , param1,(param1 + param2)// 2 , pointer )
    elif tocheck[pointer] > list[(param1 + param2)// 2]
        binarySearchStr(tocheck , list , (param1 + param2)// 2, param2 , pointer)
    else:
        binarySearchStr(tocheck , list , param1 , param2 , pointer + 1)
    