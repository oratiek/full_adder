import os
from typing import Tuple

def AND(bit1: int, bit2: int) -> int:
    return bit1 * bit2

def OR(bit1: int, bit2: int) -> int:
    if bit1 or bit2:
        return 1
    else:
        return 0

def NOT(bit1: int) -> int:
    if bit1:
        return 0
    else:
        return 1

def half_adder(A: int,B: int) -> Tuple[int, int]:
    C = AND(A,B)
    S = AND(NOT(C),OR(A,B))
    return C,S

def full_adder(A: int, B: int, C0: int):
    C1,S1 = half_adder(A,B)
    C2,S2 = half_adder(S1, C0) # キャリーとサムを加算する
    
    C3 = OR(C1, C2)
    return C1, S2

def zero_pad(val: list, pad_size: int) -> list:
    return [0 for _ in range(pad_size)] + val

def ADDER(A: list, B:list, init_carry: int = 0):
    # check input size
    if len(A) != len(B):
        diff = abs(len(A) - len(B))
        if len(A) < len(B):
            A = zero_pad(A, diff)
            bit_size = len(B)
        else:
            B = zero_pad(B, diff)
            bit_size = len(B)
    else:
        bit_size = len(A)
    print("bit_size",bit_size)

    prev_carry = init_carry
    Ss = [0 for _ in range(bit_size)]
    for i in reversed(range(bit_size)):
        C, S = full_adder(A[i], B[i], prev_carry)
        Ss[i] = S
        prev_carry = C
    Ss = [prev_carry] + Ss
    return Ss

def int_to_bin(val: int) -> str:
    return "{0:b}".format(val)

def to_bit_array(binary: str) -> list:
    return [int(bit) for bit in binary]

def bin_to_int(binary: list) -> int:
    return int("".join(map(str, binary)), 2)

if __name__ == "__main__":
    a = 100
    b = 124
    A = int_to_bin(a)
    B = int_to_bin(b)
    print(f"{a} + {b}")
    Y_binary = ADDER(to_bit_array(A), to_bit_array(B))
    print("  ","".join(map(str, A)))
    print("+ ","".join(map(str, B)))
    print("---" + "-"*len(Y_binary))
    print(" ","".join(map(str, Y_binary)))

    Y_int = bin_to_int(Y_binary)
    print(Y_int)



