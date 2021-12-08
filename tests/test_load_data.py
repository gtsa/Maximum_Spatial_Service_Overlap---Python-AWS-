import numpy as np
import pytest

from load_data import load_data

def mock_input(monkeypatch, data):
    responses = iter(data)
    monkeypatch.setattr('builtins.input', lambda: next(responses, '\n'))

def test_load_data_successfully(monkeypatch):
    mock_input(monkeypatch, ['5 2', '3 3 2', '1 1 2'])
    a, b = load_data()
    assert (a, b) == (5, [[3, 3, 2], [1, 1, 2]])

def test_load_validation_missing_input_arg(monkeypatch):
    mock_input(monkeypatch, ['5 ', '3 3 2', '1 1 2'])
    with pytest.raises(ValueError):
        load_data()