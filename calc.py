## 함수 선언부(=메소드)
def add_func(n1, n2) :
    retValue = n1 + n2
    return retValue

def sub_func(n1, n2) :
    retValue = n1 - n2
    return retValue

def mul_func(n1, n2) :
    retValue = n1 * n2
    return retValue

def div_func(n1, n2) :
    retValue = n1 / n2
    return retValue

def dmul_func(n1) :
    retValue = n1 * n1
    return retValue



## 전역 변수부
num1, num2, result = 100, 200, 0





## 메인 코드부
result = add_func(num1, num2)
print(num1, "+", num2, "=", result)

result = sub_func(num1, num2)
print(num1, "-", num2, "=", result)

result = mul_func(num1, num2)
print(num1, "*", num2, "=", result)

result = div_func(num1, num2)
print(num1, "/", num2, "=", result)

result = dmul_func(num1)
print(num1, "*", num1, "=", result)
