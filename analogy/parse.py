
def parse_txt(txt, normalize):
    ret = {}
    cat = None
    n = len(txt)
    ix = 0
    end = txt.find('\n', ix)
    while ix < n:
        line = txt[ix:end].strip()
        if line[0] == ':':
            cat = line[1:].strip()
            ret[cat] = []
        elif line[0] == '#':
            pass
        else:
            [a, b, c, d] = [normalize(w) for w in line.split()]
            ret[cat].append((a, b, c, d))
        ix = end + 1
        end = txt.find('\n', ix)
    return ret
