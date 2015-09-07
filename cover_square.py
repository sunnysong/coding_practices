def cover_square(n, m, a):
    """
    Theatre Square in the capital city of Berland has a rectangular shape
    with the size n × m meters. On the occasion of the city's anniversary,
    a decision was taken to pave the Square with square granite flagstones.
    Each flagstone is of the size a × a.

    What is the least number of flagstones needed to pave the Square?
    It's allowed to cover the surface larger than the Theatre Square,
    but the Square has to be covered. It's not allowed to break
    the flagstones. The sides of flagstones should be parallel to
    the sides of the Square.

    The input contains three positive integer numbers
    in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).
    """
    rows, mod = divmod(n, a)
    if mod:
        rows += 1
    cols, mod = divmod(m, a)
    if mod:
        cols += 1
    return cols * rows

handle = input()
n, m, a = [int(i) for i in handle.split()]
print(cover_square(n, m, a))
