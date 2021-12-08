import numpy as np


def get_city_grid_coords(city_dim):
    city_grid_coords = np.indices((city_dim, city_dim))
    city_grid_coords = city_grid_coords.reshape(2, -1)
    city_grid_coords = city_grid_coords.T
    return city_grid_coords


def pythonize_coords(xy_coords, grid_dim):
    xy_coords = np.array(xy_coords)
    xy_coords[0] = (grid_dim + 1) - xy_coords[0]
    pythonic_coords =  xy_coords[1] - 1#TO-DO : περιγραφη γεωμετριας, σπασιμο, neat
    return pythonic_coords


def get_pizzeria_cover_grid(city_grid_coords, pizzeria_location, service_cover):
    distance_from_pizzeria_grid_coords = city_grid_coords - pizzeria_location
    distance_from_pizzeria_grid_coords
    distance_from_pizzeria_grid = np.abs(distance_from_pizzeria_grid_coords).sum(1)
    covered_coords = city_grid_coords[distance_from_pizzeria_grid <= service_cover]
    city_dim = int(len(city_grid_coords)**.5)
    pizzeria_cover_grid = np.zeros((city_dim, city_dim), dtype=int)#ΤΟΔΟ APLOPOISI?
    for i in covered_coords:
        pizzeria_cover_grid[tuple(i)] = 1
    return pizzeria_cover_grid


def get_max_grids_overlap(grids):
    resulting_grid = 0
    for grid in grids:
        resulting_grid += grid
    return np.amax(resulting_grid)