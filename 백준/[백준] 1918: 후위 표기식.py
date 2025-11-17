import sys
input = sys.stdin.readline

expression = list(input().strip())
operator = ('+', '-', '*', '/')
answer = []
no_bracket_exp = [] # 괄호를 모두 제거한 수식 저장

# 괄호가 없는 수식을 후위 연산자 표기로 바꾸기
def make_postfix(exp):
    operand_stack = []
    operator_stack = []
    result = []

    for e in exp:
        # 연산자인 경우
        if e in operator:
            operator_stack.append(e)

        # 피연산자인 경우
        else:
            # 곱하기 또는 나누기 먼저 해주기
            if operator_stack and operator_stack[-1] in '*/':
                o1 = operand_stack.pop()
                o2 = e
                op = operator_stack.pop()

                operand_stack.append(o1 + o2 + op)
            else:
                operand_stack.append(e)

    # 첫 피연산자 저장
    result.append(operand_stack[0])

    # 더하기 또는 빼기
    for i in range(len(operand_stack) - 1):
        result.append(operand_stack[i + 1])
        result.append(operator_stack[i])

    return ''.join(result)

for e in expression:
    in_bracket = []

    # 닫힌 괄호가 나왔다면
    if e == ')':
        # 열린 괄호가 나올 때까지 수식 추출
        while no_bracket_exp[-1] != '(':
            in_bracket.append(no_bracket_exp.pop())

        # 스택에서 역순으로 추출되므로 뒤집어주기
        in_bracket.reverse()

        # 열린 괄호 빼주기
        no_bracket_exp.pop()

        # 후위 연산자 식으로 바꿔서 넣어주기
        no_bracket_exp.append(make_postfix(in_bracket))
    else:
        no_bracket_exp.append(e)

print(make_postfix(no_bracket_exp))
