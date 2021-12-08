import numpy as np
import pytest

from functions import get_city_grid_coords, pythonize_coords, get_pizzeria_cover_grid, get_max_grids_overlap
from test_load_data import mock_input

def test_get_city_grid_coords():
    a = get_city_grid_coords(2)
    b = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    assert np.array_equal(a, b)
