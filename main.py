import numpy as np
from load_data import load_data
from functions import get_city_grid_coords, pythonize_coords, get_pizzeria_cover_grid, get_max_grids_overlap


def get_max_pizza_overlap():
    """
    Compute max_pizza_overlap starting from console input,
    transforming the data so as to pass from cartesian coords to pythonic indexes,
    creating a matrix (2D-numpy.array) to represent each pizzeria's service cover,
    finally adding these same dimension matrices up and finding this sum's maximum
    return: int
    """
    city_dim, pizzerias = load_data()
    city_grid_coords = get_city_grid_coords(city_dim)
    all_pizzerias_cover_grids = []
    for pizzeria in pizzerias:
        location = pythonize_coords(pizzeria[:2], city_dim)
        service_cover = pizzeria[2]
        pizzeria_cover_grid = get_pizzeria_cover_grid(city_grid_coords, location, service_cover)
        all_pizzerias_cover_grids.append(pizzeria_cover_grid)
    max_pizza_overlap = get_max_grids_overlap(all_pizzerias_cover_grids)
    return max_pizza_overlap


if __name__ == "__main__":
    print(get_max_pizza_overlap())
