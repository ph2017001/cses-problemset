def permute(a, l, r, res):
    if l == r:
        res.add(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, res)
            a[l], a[i] = a[i], a[l]  # backtrack


if __name__ == "__main__":
    string = input()
    res = {string}
    n = len(string)
    a = list(string)
    permute(a, 0, n - 1, res)
    res = sorted(res)
    print(len(res))
    for i in res:
        print(i)

