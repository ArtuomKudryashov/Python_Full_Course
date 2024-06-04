def route_info(route):
    if "distance" in route and type(route['distance']) == int:
        return f"Distance to your destination is {route['distance']}"
    elif "distance" in route and type(route['distance']) != int:
        return "Invalid route data"
    elif 'speed' in route and 'time' in route:
        if type(route['speed']) == int and type(route['time']) == int:
            return f"Distance to your destination is {route['speed'] * route['time']}"
        else:
            return "Invalid route data"
    else:
        return "No distance info is available"


print(route_info({'distance': 15}))

route_info_with = {
    "distance": 30,
    "speed": 30.4,
    "time": 4
}

route_info_with['distance'] = 40

route_info_without = {
    "speed": 30,
    "time": 4
}
route_my_spead = {
    "my_spead": 30

}
route_dis={
    "speed": 30,
    "time": 4

}

print(route_info(route_info_with))
print(route_info(route_info_without))
print(route_info(route_my_spead))
print(route_info(route_dis))
