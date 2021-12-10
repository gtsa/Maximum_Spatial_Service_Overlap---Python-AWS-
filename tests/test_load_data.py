import numpy as np
import pytest

from load_data import load_data

def mock_input(monkeypatch, data):
    """
    Helper function mocks the built-in input function
    via monkeypatch fixture
    :param data: subsitute for console input data
    """
    responses = iter(data)
    monkeypatch.setattr('builtins.input', lambda: next(responses, '\n'))

def test_load_data_use_case(monkeypatch):
    """
    Test load_data via console in a use case
    :param monkeypatch: subsitute for console input data
    """
    mock_input(monkeypatch, ['5 2', '3 3 2', '1 1 2'])
    a, b = load_data()
    assert (a, b) == (5, [[3, 3, 2], [1, 1, 2]])


@pytest.mark.parametrize("x", ['', '5', '5 2'])
@pytest.mark.parametrize("y", ['3 3 2', '3 2', '3', ''])
@pytest.mark.parametrize("z", ['1 1 2', '1 1', '1', ''])
def test_load_validation_edge_case_missing_input_arg(monkeypatch, x, y, z):
    """
    Test load_data via console in a the edge case where
    the first line input has less values than expected
    :param monkeypatch: subsitute for console input data
    """
    if x == '5 2' and y == '3 3 2' and z == '1 1 2':
        pass
    else:
        inp = [x]+[y]+[z]
        mock_input(monkeypatch, inp)
        with pytest.raises(ValueError):
            load_data()

@pytest.mark.parametrize("x", [['0 2', '3 3 2', '1 1 2'],
                               ['1001 2', '3 3 2', '1 1 2'],
                               ['5 0', '3 3 2', '1 1 2'],
                               ['5 1001', '3 3 2', '1 1 2'],
                               ['5 2', '0 3 2', '1 1 2'],
                               ['5 2', '1001 3 2', '1 1 2'],
                               ['5 2', '3 0 2', '1 1 2'],
                               ['5 2', '3 1001 2', '1 1 2'],
                               ['5 2', '3 3 0', '1 1 2'],
                               ['5 2', '3 3 1001', '1 1 2'],
                               ['5 2', '3 3 2', '0 1 2'],
                               ['5 2', '3 3 2', '1001 1 2'],
                               ['5 2', '3 3 2', '1 0 2'],
                               ['5 2', '3 3 2', '1 1001 2'],
                               ['5 2', '3 3 2', '1 1 0'],
                               ['5 2', '3 3 2', '1 1 1001']])
def test_load_validation_edge_case_missing_input_arg(monkeypatch, x):
    """
    Test load_data via console in a the edge case where
    the first line input has less values than expected
    :param monkeypatch: subsitute for console input data
    """
    mock_input(monkeypatch, x)
    with pytest.raises(Exception):
        load_data()