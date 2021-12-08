import numpy as np

class Pizzeria_info:
    # necessary methods
    def __init__(self, city_dim, location, service_cover):
        self.city_dim = city_dim
        self.location = location
        location_x_coord = city_dim + 1 - self.location[0]
        location_y_coord = self.location[1]
        self.zero_indexed_location = tuple([i - 1 for i in (location_x_coord, location_y_coord)])
        self.service_cover = service_cover

    def service_cover_on_city_map(self):
        self.city_grid = np.zeros((self.city_dim, self.city_dim), dtype=int)
        self.city_grid_coords = np.indices(self.city_grid.shape).reshape(2, -1).T
        pizzeria_indexed_grid_coords = self.city_grid_coords - np.array(self.zero_indexed_location)
        distance_from_pizzeria_grid = np.abs(pizzeria_indexed_grid_coords).sum(1)
        self.covered_coords = self.city_grid_coords[distance_from_pizzeria_grid <= int(self.service_cover)]
        self.service_covered_grid = np.zeros((self.city_dim, self.city_dim), dtype=int)
        for i in self.covered_coords:
            self.service_covered_grid[tuple(i)] = 1
        return self.service_covered_grid

    # not necessary methods, potentially useful for future functionality
    def viz_locate_on_city_map(self):
        self.city_grid = np.zeros((self.city_dim, self.city_dim), dtype=int)
        self.city_grid[self.zero_indexed_location] = 1
        return self.city_grid

    def viz_service_cover_on_city_map(self):
        print(self.service_cover_on_city_map())

def max_grids_overlap(grids):
    result_grid = 0
    for grid in grids:
        #print(grid)
        result_grid += grid
    #print(result_grid)
    return np.amax(result_grid)

def load_data():
    #_N, _M = input('Give N and M value (separated by a space, i.e. "N M"): \n').split()
    _N, _M = input().split()
    N, M = int(_N), int(_M)
    #P = [input(f'Give info for pizzeria n°{i+1} (separated by a space, i.e. "x y max_service_distance"): \n').split() for i in range(M)]
    P = [input().split() for i in range(M)]
    for ind, lst in enumerate(P):
        P[ind] = list(map(int, lst))
    return (N, P)

def find_max():
    N, pizzerias = load_data()
    all_pizzerias_cover_areas = []
    for pizzeria in pizzerias:
        pizzeria_info = Pizzeria_info(N, pizzeria[:2], pizzeria[2])
        each_pizzeria_cover_area = pizzeria_info.service_cover_on_city_map()
        all_pizzerias_cover_areas.append(each_pizzeria_cover_area)
    return max_grids_overlap(all_pizzerias_cover_areas)

if __name__ == "__main__":
    print(find_max())