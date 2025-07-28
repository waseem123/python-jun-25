def sort_list(data, ascending=True):
    if ascending:
        data.sort()
    else:
        data.sort(reverse=True)
    return data