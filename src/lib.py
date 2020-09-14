import re

def detect_numbers(req: str):
    nbs = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", req)
    if len(nbs) == 0:
        return None
    n = nbs[0]
    pos = req.find(str(n))
    s = req[pos:]
    s = s.split(' ', 2)
    return s[0]