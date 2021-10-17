def parcours(l):
    #Get a sorted version of the list
    sorted_l = sorted(l)
    #Get value in list closer to 0, start in middle of list
    min_val, idx = min([(abs(val), idx) for (idx, val) in enumerate(sorted_l)])
    #split list in idx and revert position of left side
    final_list = sorted(sorted_l[:idx], key=None, reverse=True)
    final_list+=(sorted_l[idx:])
    return final_list