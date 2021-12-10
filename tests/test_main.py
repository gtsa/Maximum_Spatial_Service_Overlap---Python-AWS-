import numpy as np
import random
import json
import pytest

from main import get_max_pizza_overlap
from tests.test_load_data import mock_input


def test_main_usual_case(monkeypatch):
    """
    Test main function for successful use case ['5 2', '3 3 2', '1 1 2']
    (using monkeypatch to mock the input)
    """

    mock_input(monkeypatch, ['5 2', '3 3 2', '1 1 2'])
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
        inp = [str(n) + " " + str(m)] + [" ".join([str(random.randint(1, n)) for i in range(3)]) for j in range(m)]
        mock_input(monkeypatch, inp)
        assert get_max_pizza_overlap() <= m

@pytest.mark.slow
def test_main_stress(monkeypatch):
    """
    Stress test main function for the limit values N, M =1000 and X, Y, K in [1, 1000]
    (using monkeypatch to mock the input)
    """
    with open('tests/stress_test_input.json') as f:
        stress_test_input = json.load(f)
    mock_input(monkeypatch, stress_test_input)
    assert get_max_pizza_overlap() == 528