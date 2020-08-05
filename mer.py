def merge_two_sorted_lists(a, b):
    """Merge two lists that are already sorted."""
    c = []

    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))

    # One of the arrays is now empty
    if a and not b:
        c.extend(a)
    elif b and not a:
        c.extend(b)

    return list(map(str, c))


if __name__ == "__main__":
    f = open("rosalind_mer.txt", "r")
    f.readline()
    a1 = f.readline()
    f.readline()
    b1 = f.readline()
    a1 = list(map(int, a1.split()))
    b1 = list(map(int, b1.split()))
    z = " ".join(s for s in merge_two_sorted_lists(a1, b1))
    fw = open("mer-output.txt", "w")
    fw.write(z)
    
