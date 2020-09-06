


'''
Exercise 3 (3 points). Now write a function get_route(segs, origin) that traces the complete itinerary of the pilot, given her first port of origin. Assume that the destination for a flight is the same as the origin for the next flight. The itinerary is completed when he arrives back at the starting port of origin. For example, if the starting port is "JFK", your function should return the list: ["JFK", "DEN", "SFO", "LAS", "LAX", "ORD", "ATL"].
'''

segments = [("JFK", "DEN"), ("LAX", "ORD"), ("DEN", "SFO"), ("LAS", "LAX"), ("ORD", "ATL"), ("ATL", "JFK"), ("SFO", "LAS")]
start = "JFK"

import random
def get_route(path, origin):

    
    startSeg = [i[0] for i in segments]
    endSeg = [i[1] for i in segments]

    startPath = origin
    
    itinerary_list =[]
    endPath == ""      
        
    while endPath != origin :

        endPath == ""      
        
        try:

            startSegIndex = startSeg.index(startPath)
            endPath = endSeg[startSegIndex]
            itinerary_list.append(startPath)
            startPath = endPath
        except:
            return "No valid path"
    return itinerary_list


def find_dest(segs, origin):
    assert type(origin) is str
    assert type(segs) is list
    dest = [item[1] for item in segs if item[0] == origin]
    return ' ' .join(dest)
    
    
import random
# Test pilot route
ports = ["JFK", "DEN", "SFO", "LAS", "LAX", "ORD", "ATL"]
starting_port = random.sample(ports, 5)
print(starting_port)
for p in starting_port:
     itinerary = get_route(segments, p)
     assert itinerary[0] == p, "incorrect port of origin for the itinerary"
     for i, port in enumerate(itinerary[:-1]):
         dest = find_dest(segments, port)
         print(dest)
         assert dest == itinerary[i+1], "incorrect itinerary"
print("\n(Passed.)")

