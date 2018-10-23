def isValidWalk(walk):
    from collections import Counter
    d = Counter(walk)
    ns = abs(d["n"] - d["s"])
    we = abs(d["w"] - d["e"])
    back = int(ns + we)
    forward = len(walk)
    if (10-(forward+back))>=0:
        if(ns == 0 and we == 0):
            return(True)
        else:
            return(False)
    else:
        return(False)

walk = ["s", "n", "w", "w", "n", "s", "e", "e"]
isValidWalk(walk)
