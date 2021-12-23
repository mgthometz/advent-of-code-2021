from collections import namedtuple


class Digit:
    def __init__(self, value, n_segments):
        self.value = value
        self.n_segments = n_segments
        self.segment_chars = None


class Zero(Digit):
    def __init__(self):
        super().__init__(0, 6)
        self.segments = set([0, 1, 2, 4, 5, 6])


class One(Digit):
    def __init__(self):
        super().__init__(1, 2)
        self.segments = set([2, 5])

    

class Two(Digit):
    def __init__(self):
        super().__init__(2, 5)
        self.segments = set([0, 2, 3, 4, 6])


class Three(Digit):
    def __init__(self):
        super().__init__(3, 5)
        self.segments = set([0, 2, 3, 5, 6])


class Four(Digit):
    def __init__(self):
        super().__init__(4, 4)
        self.segments = set([1, 2, 3, 5, 6])
        self.segment_chars = None


class Five(Digit):
    def __init__(self):
        super().__init__(5, 5)
        self.segments = set([0, 1, 3, 5, 6])


class Six(Digit):
    def __init__(self):
        super().__init__(6, 6)
        self.segments = set([0, 1, 3, 4, 5, 6])


class Seven(Digit):
    def __init__(self):
        super().__init__(7, 3)
        self.segments = set([0, 2, 5])
        self.segment_chars = None


class Eight(Digit):
    def __init__(self):
        super().__init__(8, 7)
        self.segments = set([0, 1, 2, 3, 4, 5, 6])
        self.segment_chars = None


class Nine(Digit):
    def __init__(self):
        super().__init__(9, 6)
        self.segments = set([0, 1, 2, 3, 4, 6])


with open('src/day8/input.txt') as f:
    raw = [l.split('|') for l in f.readlines()]

Obs = namedtuple('Obs', 'patterns output')
data = [Obs(r[0].strip().split(), r[1].strip().split()) for r in raw]


def decode(obs):
    one = One()
    four = Four()
    seven = Seven()
    eight = Eight()
    search = [one, four, seven, eight]
    digits = []
    for ob in obs:
        if search:
            for idx, s in enumerate(search):
                if s.n_segments == len(ob):
                    s.segment_chars = set(list(ob))
                    digits.append(s)
                    search.pop(idx)

    segment_map = dict.fromkeys(range(7))
    segment_map[0] = seven.segment_chars.difference(one.segment_chars).pop()

    # Determine nine segment chars
    nine = Nine()
    comparison = four.segment_chars.union(seven.segment_chars)
    for ob in obs:
        n_chars = len(ob)
        ob_chars = set(list(ob))
        diff = ob_chars.difference(comparison)
        if (n_chars==6) and (len(diff)==1):
            nine.segment_chars = ob_chars
            digits.append(nine)
            segment_map[6] = diff.pop()
            break

    segment_map[4] = eight.segment_chars.difference(nine.segment_chars).pop()

    # Determine zero segment chars
    zero = Zero()
    for ob in obs:
        n_chars = len(ob)
        ob_chars = set(list(ob))
        diff = one.segment_chars.difference(ob_chars)
        if (n_chars==6) and (len(diff)==0) and ob_chars!=nine.segment_chars:
            zero.segment_chars = ob_chars
            digits.append(zero)
            break
    
    segment_map[3] = eight.segment_chars.difference(zero.segment_chars).pop()
    
    # Determine six 
    six = Six()
    for ob in obs:
        n_chars = len(ob)
        ob_chars = set(list(ob))
        if (n_chars==6) and (ob_chars!=nine.segment_chars) and (ob_chars!=zero.segment_chars):
            six.segment_chars = ob_chars
            digits.append(six)
            break

    five = Five()
    five.segment_chars = six.segment_chars.difference(segment_map[4])
    digits.append(five)
    
    three = Three()
    for ob in obs:
        n_chars = len(ob)
        ob_chars = set(list(ob))
        inter = one.segment_chars.intersection(ob_chars)
        if (n_chars==5) and len(inter)==2:
            three.segment_chars = ob_chars
            digits.append(three)
        
    two = Two()
    for ob in obs:
        n_chars = len(ob)
        ob_chars = set(list(ob))
        if (n_chars==5) and (ob_chars!=five.segment_chars) and (ob_chars!=three.segment_chars):
            two.segment_chars = ob_chars
            digits.append(two)

    return digits


matches = []
for d in data:
    digits = decode(d.patterns)
    final = ''
    for out in d.output:
        for digit in digits:
            comparison = set(list(out))
            dig_comp = digit.segment_chars
            if comparison == digit.segment_chars:
                final += str(digit.value)
    matches.append(int(final))

    
print(sum(matches))