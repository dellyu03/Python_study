import re
p = re.compile("ca.e")
def print_match(m):
    if m:
        print("m.group():, m.group()")
        print("m.string:", m.string)
        print("m.end():", m.start())
        print("m.span():", m.span())
    else:
        print("매칭되지 않음")
    m = p.match("careless")
    print_match(m)
    print()

    m = p.search("good care")
    print_match(m)