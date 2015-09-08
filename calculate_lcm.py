def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm_(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcm(*args):
    """Return lcm of args."""
    return reduce(lcm_, args)
total = 0
for i in range(1000):
  if i % 3 == 0 or i % 5 == 0:
    total += i
print(total)