import numpy as np
import random
import json
import pytest
import io

from main import get_max_pizza_overlap

def test_main_usual_case(monkeypatch):
    """
    Test main function for successful use case ['5 2', '3 3 2', '1 1 2']
    (using monkeypatch to mock the input)
    """
    monkeypatch.setattr('sys.stdin', io.StringIO('5 2\n3 3 2\n1 1 2\n'))
    assert get_max_pizza_overlap() == 2



def test_main_edge_case(monkeypatch):
    """
    Test main function' output to be always is less than or equal to pizzeria's number (max_pizza_overlap <= M)
    (5 loops with random generated N, M, X, Y, K in [1,10],
    using monkeypatch to mock the input)
    """
    for iteration in range(5):
        n = random.randint(1, 10)
        m = random.randint(1, 10)
        inp = str(n) + " " + str(m) +"\n"+"\n".join([" ".join([str(random.randint(1, n)) for i in range(3)]) for j in range(m)])+"\n"
        monkeypatch.setattr('sys.stdin', io.StringIO(inp))
        assert get_max_pizza_overlap() <= m

@pytest.mark.slow
def test_main_stress(monkeypatch):
    """
    Stress test main function for the limit values N, M =1000 and X, Y, K in [1, 1000]
    (using monkeypatch to mock the input)
    """
    with open('tests/stress_test_input.json') as f:
        stress_test_input = json.load(f)
    inp = "\n".join(["".join(i) for i in stress_test_input]) + "\n"
    monkeypatch.setattr('sys.stdin', io.StringIO(inp))
    assert get_max_pizza_overlap() == 528
