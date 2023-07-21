def get_details(**details):
    """Sample Kwargs"""
    for key, value in details.items():
        return f"{key}: {value}"
print(get_details(name="Aian", age=13))


def get_number(*args):
    """Sample Args"""
    all = []
    for a in args:
        all.append(a)
    return all

print(get_number(1, 2, 3))
