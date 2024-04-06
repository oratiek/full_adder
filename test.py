from main import *

def test_add(A: list, B: list, Y: list) -> None:
    pass_cnt = 0
    for i in range(len(A)):
        if AND(A[i], B[i]) == Y[i]:
            pass_cnt += 1
    return pass_cnt / len(A) * 100

def test_or(A: list, B: list, Y: list) -> None:
    pass_cnt = 0
    for i in range(len(A)):
        if OR(A[i], B[i]) == Y[i]:
            pass_cnt += 1
    return pass_cnt / len(A) * 100

def test_not(A: list, Y: list) -> None:
    pass_cnt = 0
    for i in range(len(A)):
        if NOT(A[i]) == Y[i]:
            pass_cnt += 1
    return pass_cnt / len(A) * 100

if __name__ == "__main__":
    A = [0,0,1,1]
    B = [0,1,0,1]

    Y = [0,0,0,1]
    and_pass_rate = test_add(A,B,Y)
    print(f"and: pass_rate {and_pass_rate}")

    Y = [0,1,1,1]
    or_pass_rate = test_or(A,B,Y)
    print(f"or: pass_rate {or_pass_rate}")
    
    A = [0,1]
    Y = [1,0]
    not_pass_rate = test_not(A,Y)
    print(f"not: pass_rate {not_pass_rate}")

