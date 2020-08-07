"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 100))
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

    # addition dict { f(a)+f(b) : a_b}
    add_comb = {}
    for i in range(len(num_set)):
        for j in range(len(num_set)-1):
            add_value = fx_lookup[num_set[i]] + fx_lookup[num_set[j]]
            if  add_value not in add_comb:
                add_comb[add_value] = [f"{num_set[i]}_{num_set[j]}"]
            else:
                add_comb[add_value].append(f"{num_set[i]}_{num_set[j]}")
    
    # subtraction dict {f(c)-f(d) : c_d}
    sub_comb = {}
    for i in range(len(num_set)-1, -1, -1):
        for j in range(i, -1, -1):
            sub_value = fx_lookup[num_set[i]] - fx_lookup[num_set[j]]
            if sub_value not in sub_comb:
                sub_comb[sub_value] = [f"{num_set[i]}_{num_set[j]}"]
            else:
                sub_comb[sub_value].append(f"{num_set[i]}_{num_set[j]}")
    
    # loop through addition dict
    #  if exits in subtraction dict
    #    add to result
    res = []
    for value, comb in add_comb.items():
        if value in sub_comb:
            for i in comb:
                for j in sub_comb[value]:
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
