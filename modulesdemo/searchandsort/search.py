def is_present(data, value):
    if not data:
        return False
    elif data.count(value) >= 1:
        return True
    return False
