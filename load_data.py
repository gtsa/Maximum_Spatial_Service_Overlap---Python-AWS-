def input_limits_validation(input_vars_list):
    num_input_limits_violations = sum([i not in range(1, 1001) for i in input_vars_list])
    if num_input_limits_violations > 0:
        raise Exception('Inputs must be integers and on the range [1, 1000]')


def load_data():
    _N, _M = input().split()
    N, M = int(_N), int(_M)
    input_limits_validation([N, M])
    P = []
    for i in range(M):
        _XYK = input().split()
        X, Y, K = list(map(int,(_XYK)))
        input_limits_validation([X, Y, K])
        P.append([X, Y, K])
    return (N, P)