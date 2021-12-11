import sys
from sys import stdin
import io

def input_limits_validation(input_vars_list):
    """
    Check if all variables of list are on the range [1, 1000]
    and raise Exception, if not
    :param input_vars_list -> list
    :return: None
    """
    num_input_limits_violations = sum([i not in range(1, 1001) for i in input_vars_list])
    if num_input_limits_violations > 0:
        raise Exception('Inputs must be integers and on the range [1, 1000]')


def load_data():
    """
    Load input data via standard input and transform them in digestible form
    :return: list(N:int, P:list)
    """
    A=[]
    for line in sys.stdin:
        A.append(line.split("\n")[0])
    _N, _M = A[0].split()
    N, M = int(_N), int(_M)
    input_limits_validation([N, M])
    P = []
    for i in A[1:M+1]:
        _XYK = i.split()
        X, Y, K = list(map(int,(_XYK)))
        input_limits_validation([X, Y, K])
        P.append([X, Y, K])
    return (N, P)


def load_data_():
    """
    Load input data via standard input and transform them in digestible form
    :return: list(N:int, P:list)
    """
    sys.stdin = io.StringIO('3 2\n3 3 2\n1 1 2\n')
    A=[]
    for line in sys.stdin:
        A.append(line.split("\n")[0])
    _N, _M = A[0].split()
    N, M = int(_N), int(_M)
    input_limits_validation([N, M])
    P = []
    for i in A[1:M+1]:
        _XYK = i.split()
        X, Y, K = list(map(int,(_XYK)))
        input_limits_validation([X, Y, K])
        P.append([X, Y, K])
    return (N, P)



if __name__ == "__main__":
    print(load_data())