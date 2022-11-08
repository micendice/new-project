action = str(input('enter action: '))
number_operandes = int(input('enter number of operands: '))

result_visual = ''
operand = int(input('enter 1 operand: '))
result_visual += str(operand)
result = operand 
for i in range(2, number_operandes + 1):
    print('enter', i, 'operand: ', end = '')
    operand = int(input())
    result_visual += action + str(operand) 
    if action == '+':
        result += operand
    elif action == '-':
        result -= operand
    elif action == '*':
        result *= operand
    elif action == '/':
        result /= operand
    else:
        print('Сущеглупый холоп!')
    
print(result_visual, '=', result)
print('try to change and then to commit changes')