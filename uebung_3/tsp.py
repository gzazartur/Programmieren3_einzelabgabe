import math

SHORTESTPATH = 1000000000000

def start():
    bes_st = []
    staedte_positionen = [(0.010319427306382911, 0.8956251389386756),
                          (0.6999898714299346, 0.42254500074835377),
                          (0.4294574582950912, 0.4568408794115657),
                          (0.6005454852683483, 0.9295407203370832),
                          (0.9590226056623925, 0.581453646599427),
                          (0.748521134122647, 0.5437775417153159),
                          (0.7571232013282426, 0.606435031856663),
                          (0.07528757443413125, 0.07854082131763074),
                          (0.32346175150639334, 0.7291706487873425)]
    TSP(0,bes_st, staedte_positionen)
    print(SHORTESTPATH)

def TSP(index, bes_sta, zu_bes_sta):
    global SHORTESTPATH
    bes_sta = bes_sta.copy()
    zu_bes_sta = zu_bes_sta.copy()

    bes_sta.append(zu_bes_sta[index])
    zu_bes_sta.pop(index)

    if not zu_bes_sta:
        #print(bes_sta)
        #print(zu_bes_sta)
        ges_route = route(bes_sta)
        ges_route += distance(bes_sta[0], bes_sta[len(bes_sta)-1])
        #print(ges_route)
        if ges_route < SHORTESTPATH:
            SHORTESTPATH = ges_route

        return

    for _x in range(len(zu_bes_sta)):
        TSP(_x, bes_sta, zu_bes_sta)

def distance(pos1, pos2):
    dis = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    return dis

def route(bes_sta):
    path = 0
    for x in range(len(bes_sta)-1):
        path += distance(bes_sta[x], bes_sta[x+1])

    return path
# Main program starts here
start()

