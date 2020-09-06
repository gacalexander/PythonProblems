segments = [("JFK", "DEN"), ("LAX", "ORD"), ("DEN", "SFO"), ("LAS", "LAX"), ("ORD", "ATL"), ("ATL", "JFK"), ("SFO", "LAS")]
start = "JFK"

def find_dest(segs, origin):
    assert type(origin) is str
    assert type(segs) is list
    dest = [item[1] for item in segs if item[0] == origin]
    return ' ' .join(dest)

def get_route(path, origin):
    orig_start = origin
    itinerary_list = []
    itinerary_list.append(origin)

    while len(path) >= 1:
        current = None
        directions = {}

        for item in path:

            if item[0] == origin:
                directions[item[0]] = item[1]

        if len(directions) >= 1:
            current = min(directions.values())
            remove_tuple = (origin, current)

        try:
            path.remove(remove_tuple)
            if current != orig_start:
                itinerary_list.append(current)
                origin = current
        except:
            return "not valid intinerary"

    return itinerary_list


print(get_route(segments, start))

import random
# Test pilot route
ports = ["JFK", "DEN", "SFO", "LAS", "LAX", "ORD", "ATL"]
starting_port = random.sample(ports, 5)
for p in starting_port:
     itinerary = get_route(segments, p)
     assert itinerary[0] == p, "incorrect port of origin for the itinerary"
     for i, port in enumerate(itinerary[:-1]):
         dest = find_dest(segments, port)
         print(dest)
         assert dest == itinerary[i+1], "incorrect itinerary"
print("\n(Passed.)")
