"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
fx_lookup = {}
def sumdiff(number_set):
    # convert any type to list
    num_set = list(number_set)

    # f(x) lookup_table
    for x in num_set:
        fx_lookup[x] = f(x)

    # addition dict { a_b : f(a)+f(b)}
    add_comb = {}
    i = 0
    while i < len(num_set):
        j = 0
        while j < len(num_set)-1:
            if f"{num_set[i]}_{num_set[j]}" not in add_comb:
                add_comb[f"{num_set[i]}_{num_set[j]}"] = fx_lookup[num_set[i]] + fx_lookup[num_set[j]]
            j += 1
        i += 1
    
    # subtraction dict { c_d : f(c)-f(d) }
    sub_comb = {}
    i = len(num_set)-1
    while i >= 0:
        j = len(num_set)-1
        while j >= 0:
            if f"{num_set[i]}_{num_set[j]}" not in sub_comb:
                sub_comb[f"{num_set[i]}_{num_set[j]}"] = fx_lookup[num_set[i]] - fx_lookup[num_set[j]]
            j -= 1
        i -= 1
    
    # addition dict { f(a)+f(b) : a_b}
    rev_add_comb = {}
    for key, value in add_comb.items():
        if value not in rev_add_comb:
            rev_add_comb[value] = [key]
        else:
            rev_add_comb[value].append(key)

    # subtraction dict {f(c)-f(d) : c_d}
    rev_sub_comb = {}
    for key, value in sub_comb.items():
        if value not in rev_sub_comb:
            rev_sub_comb[value] = [key]
        else:
            rev_sub_comb[value].append(key)
    
    # loop through addition dict
    #  if exits in subtraction dict
    #    add to result
    res = []
    for value, comb in rev_add_comb.items():
        if value in rev_sub_comb:
            for i in comb:
                for j in rev_sub_comb[value]:
                    res.append([i,j])

    # number of all possible combinations
    # print(len(res))

    # print all possible combinations
    for ele in res:
        ab = ele[0].split("_")
        a = int(ab[0])
        b = int(ab[1])
        cd = ele[1].split("_")
        c = int(cd[0])
        d = int(cd[1])
        formula = f"f({a}) + f({b}) = f({c}) - f({d})"
        results = f"{fx_lookup[a]} + {fx_lookup[b]} = {fx_lookup[c]} - {fx_lookup[d]}"
        print(f"{formula}{results:>30}")

sumdiff(q)
