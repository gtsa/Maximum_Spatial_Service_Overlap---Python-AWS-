import numpy as np
import json


def get_city_grid_coords(city_dim):
    """
    Create the full list of the cartesian coords for all the points
    of a square-shaped city given its side length
    :param city_dim -> int
    :return: 2d-numpy.array
    """
    city_grid_coords = np.indices((city_dim, city_dim))
    city_grid_coords = city_grid_coords.reshape(2, -1)
    city_grid_coords = city_grid_coords.T
    return city_grid_coords


def pythonize_coords(yx_coords, grid_dim):
    """
    Tranform a pair of cartsian coords into pythonic coords,
    e.g. i. inverse vertical axis/index (y/rows) (given the dimensions)
        ii. from 1-indexed to 0-indexed

    :param yx_coords -> list(int, int)
    :param grid_dim -> int
    :return: 2d-numpy.array
    """
    yx_coords = np.array(yx_coords)
    yx_coords[0] = (grid_dim + 1) - yx_coords[0]
    pythonic_coords =  yx_coords - 1#TO-DO : περιγραφη γεωμετριας, σπασιμο, neat
    return pythonic_coords


def get_pizzeria_cover_grid(city_grid_coords, pizzeria_location, service_cover):
    """
    Create the service cover grif for a pizzeria,
    given its city's coors, as well as its location/coords and delivery radius
    :param city_grid_coords -> 2d-numpy.array
    :param pizzeria_location -> 2d-numpy.array
    :param service_cover -> int
    :return: 2d-numpy.array
    """
    distance_from_pizzeria_grid_coords = city_grid_coords - pizzeria_location
    distance_from_pizzeria_grid = np.abs(distance_from_pizzeria_grid_coords).sum(1)
    covered_coords = city_grid_coords[distance_from_pizzeria_grid <= service_cover]
    city_dim = int(len(city_grid_coords)**.5)
    pizzeria_cover_grid = np.zeros((city_dim, city_dim), dtype=int)#ΤΟΔΟ APLOPOISI?
    for i in covered_coords:
        pizzeria_cover_grid[tuple(i)] = 1
    return pizzeria_cover_grid


def get_max_grids_overlap(grids):
    """
    Add up a list of same dimensio np.arrays,
    andfind the maximum element of this sum
    :param grids -> 2d-numpy.array
    :return: int
    """
    resulting_grid = 0
    for grid in grids:
        resulting_grid += grid
    return np.amax(resulting_grid)

def get_max_pizza_overlap(event, context):
    """
    Compute max_pizza_overlap starting from inline json POST body input,
    transforming the data so as to pass from cartesian coords to pythonic indexes,
    creating a matrix (2D-numpy.array) to represent each pizzeria's service cover,
    finally adding these same dimension matrices up and finding this sum's maximum
    return: int
    """
    request_body = json.loads(event["body"])
    N = int(request_body["N"])
    P = [tuple(pizzeria_row) for pizzeria_row in request_body["P"]]
    city_dim, pizzerias = N, P
    city_grid_coords = get_city_grid_coords(city_dim)
    all_pizzerias_cover_grids = []
    for pizzeria in pizzerias:
        location = pythonize_coords(pizzeria[:2], city_dim)
        service_cover = pizzeria[2]
        pizzeria_cover_grid = get_pizzeria_cover_grid(city_grid_coords, location, service_cover)
        all_pizzerias_cover_grids.append(pizzeria_cover_grid)
    max_pizza_overlap = get_max_grids_overlap(all_pizzerias_cover_grids)

    print("Maximum pizza overlap possible")
    print(max_pizza_overlap)
    response_body = {
        "Maximum pizza overlap possible": int(max_pizza_overlap)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

    return response
