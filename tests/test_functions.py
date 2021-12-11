import numpy as np
import io
import pytest

from functions import get_city_grid_coords, pythonize_coords, get_pizzeria_cover_grid, get_max_grids_overlap

def test_get_city_grid_coords_use_case():
    """
    Test get_city_grid_coords() for use case
    """
    a = get_city_grid_coords(2)
    b = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    assert np.array_equal(a, b)


@pytest.mark.parametrize("x", ["", " "])
def test_get_city_grid_coords_edge_case(x):
    """
    Test get_city_grid_coords() for use case
    """
    with pytest.raises(TypeError):
        get_city_grid_coords(x)


def test_pythonize_coords_use_case():
    """
    Test pythonize_coords() for use case
    """
    a = pythonize_coords([3, 3], 5)
    b = np.array([2, 2])
    assert np.array_equal(a, b)



def test_get_pizzeria_cover_grid_use_case():
    """
    Test get_pizzeria_cover_grid() for use case
    """
    city_grid_coords = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
    pizzeria_location = np.array([[1, 1]])
    service_cover = 1
    a = get_pizzeria_cover_grid(city_grid_coords, pizzeria_location, service_cover)
    b = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0] ])
    assert np.array_equal(a, b)


def test_get_max_grids_overlap_usue_case():
    """
    Test get_max_grids_overlap() for use case
    """
    a = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    b = np.array([[1, 1, 2], [3, 1, 1], [0, 5, 0]])
    c = np.array([[0, 1, 8], [2, 1, 1], [3, 1, 0]])
    d = np.array([[1, 1, 0], [0, 0, 4], [0, 1, 7]])
    grids = np.array([a, b , c, d])
    assert get_max_grids_overlap(grids) == 10