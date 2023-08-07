from collections.abc import Hashable


def turn_kwargs_to_dict(**kwargs) -> dict:
    kwargs_dict = {}
    for key, value in kwargs.items():
        kwargs_dict[value if isinstance(value, Hashable) else str(value)] = key
    return kwargs_dict


print(turn_kwargs_to_dict(res=1, reverse=[1, 2, 3]))
