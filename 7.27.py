def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if _name_ == '_main_':
 start_num = int(input())
 print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
