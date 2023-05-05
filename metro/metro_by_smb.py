from math import radians, cos, sin, asin


def distance_haversine(point_1: tuple, point_2: tuple):
    d_earth = 2.0 * 6372.8
    lat1, long1 = tuple(radians(c) for c in point_1)
    lat2, long2 = tuple(radians(c) for c in point_2)
    d = sin((lat2 - lat1) / 2.0) ** 2.0 + cos(lat1) * cos(lat2) * sin(
        (long2 - long1) / 2.0) ** 2.0
    return d_earth * asin(d ** 0.5)


def find_nearest(point_1: tuple, points: dict):
    dists = {p: distance_haversine(point_1, points[p]) for p in points}
    name, dist = min(dists.items(), key=lambda d: d[1])
    return {'name': name, 'distance': dist,
            'dist_coef': 3 if dist <= 1.0 else 2 if dist < 2.0 else 1}


# metro_points = {
#     'Новокосино': (55.745113, 37.864052),
#     'Перово': (55.75098, 37.78422),
#     'Ховрино': (55.8777, 37.4877),
#     }

# point_1 = (55.741298984107324, 37.415756143334846)
# print(find_nearest(point_1, metro_points))
# {'name': 'Ховрино', 'distance': 15.823760672698684, 'dist_coef': 1}
