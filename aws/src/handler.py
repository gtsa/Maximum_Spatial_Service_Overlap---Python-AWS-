import json
import numpy as np
#from find_max import max_pizza_overlap

class pizzeria_info:
    def __init__(self, city_dim, location, service_cover):
        self.city_dim = city_dim
        self.location = location
        self.zero_indexed_location = tuple([i - 1 for i in (city_dim + 1 - self.location[0], self.location[1])])
        self.service_cover = service_cover

    def viz_locate_on_city_map(self):
        self.city_grid = np.zeros((self.city_dim, self.city_dim), dtype=int)
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

def get_max_pizza_overlap(event, context):
    request_body = json.loads(event["body"])
    N = int(request_body["N"])
    P = [tuple(pizzeria_row) for pizzeria_row in request_body["P"]]
    
    max = max_pizza_overlap(N, P)
    
    print("max")
    print(max)
    
    response_body = {
        "max": int(max)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

    return response
