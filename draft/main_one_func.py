import numpy as np

def find_max_3_functions_():
    _city_dim, _M = input('Give N and M value (separated by a space, i.e. "N M"): ').split()
    #_N, _M = input().split()
    city_dim, M = int(_city_dim), int(_M)
    pizzerias = [input(f'Give info for pizzeria n°{i+1} (separated by a space, i.e. "x y max_service_distance"): ').split() for i in range(M)]
    #P = [input().split() for i in range(M)]
    for ind,lst in enumerate(pizzerias):
        pizzerias[ind] = list(map(int, lst))
    city_grid = np.zeros((city_dim, city_dim), dtype=int)
    city_grid_coords = np.indices(city_grid.shape).reshape(2, -1).T
    overlap_grids = 0
    for pizzeria in pizzerias:
        location_x_coord = city_dim + 1 - pizzeria[0]
        location_y_coord = pizzeria[1]
        zero_indexed_location = tuple([i - 1 for i in (location_x_coord, location_y_coord)])
        pizzeria_indexed_grid_coords = city_grid_coords - np.array(zero_indexed_location)
        distance_from_pizzeria_grid = np.abs(pizzeria_indexed_grid_coords).sum(1)
        covered_coords = city_grid_coords[distance_from_pizzeria_grid <= int(pizzeria[2])]
        service_covered_grid = np.zeros((city_dim, city_dim), dtype=int)
        for i in covered_coords:
            service_covered_grid[tuple(i)] = 1
        print(service_covered_grid)
        overlap_grids += service_covered_grid
    print(overlap_grids)
    return np.amax(overlap_grids)

if __name__ == "__main__":
    find_max_3_functions
