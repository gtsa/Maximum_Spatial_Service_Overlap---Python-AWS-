import numpy as np

class pizzeria_info:
    def __init__(self, city_dim, location, service_cover):
        self.city_dim = city_dim
        self.location = location
        self.zero_indexed_location = tuple([i - 1 for i in (N + 1 - self.location[0], self.location[1])])
        self.service_cover = service_cover

    def viz_locate_on_city_map(self):
        self.city_grid = np.zeros((N, N), dtype=int)
        self.city_grid[self.zero_indexed_location] = 1
        return self.city_grid

    def service_cover_on_city_map(self):
        self.city_grid = np.zeros((self.city_dim, self.city_dim), dtype=int)
        self.city_grid_coords = np.indices(self.city_grid.shape).reshape(2, -1).T
        distance_from_pizzeria = np.abs(self.city_grid_coords - np.array(self.zero_indexed_location)).sum(1)
        self.covered_coords = self.city_grid_coords[distance_from_pizzeria <= int(self.service_cover)]
        self.service_covered_grid = np.zeros((self.city_dim, self.city_dim), dtype=int)
        for i in self.covered_coords:
            self.service_covered_grid[tuple(i)] = 1
        return self.service_covered_grid

    def viz_service_cover_on_city_map(self):
        print(self.service_cover_on_city_map())

def max_pizza_overlap(N, pizzerias):
    result_grid = 0
    for piz in pizzerias:
        # print(pizzeria_info(N, piz[:2], piz[2]).service_cover_on_city_map())
        result_grid = result_grid + pizzeria_info(N, piz[:2], piz[2]).service_cover_on_city_map()
    # print(result_grid)
    return np.amax(result_grid)

def load_data():
    # _N, _M = input('Give N and M value (separated by a space, i.e. "N M"): ').split()
    _N, _M = input().split()
    N, M = int(_N), int(_M)
    # P = [input(f'Give info for pizzeria n°{i+1} (separated by a space, i.e. "x y max_service_distance"): ').split() for i in range(M)]
    P = [input().split() for i in range(M)]
    for ind, lst in enumerate(P):
        P[ind] = list(map(int, lst))
    return (N, P)

def find_max():
    N, pizzerias = load_data()
    return max_pizza_overlap(N, pizzerias)

