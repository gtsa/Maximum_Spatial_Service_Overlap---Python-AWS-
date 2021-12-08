import numpy as np
import pytest

from main import get_max_pizza_overlap
from test_load_data import mock_input

def test_main(monkeypatch):
    mock_input(monkeypatch, ['5 2', '3 3 2', '1 1 2'])
    assert get_max_pizza_overlap() == 2

def test_main_stress(monkeypatch):
    # TODO: generate 1000 lines
    mock_input(monkeypatch, ['5 2', '3 3 2', '1 1 2'])
    assert get_max_pizza_overlap() == 2