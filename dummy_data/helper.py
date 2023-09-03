import random
import string
from dummy_data import constants as const

from collections import namedtuple


def get_random_id(N=8, prefix="") -> str:
    """Generates random id with given prefix in lowwr case
    param: N: given lenght of string, defualt is 8
    param: prefix: given prefix to start the string with, defaul is empty
    """
    return f"{prefix}_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=N))


def get_random_float(start=1, end=99, decimal=3) -> int:
    """generate random float value
    param: start: start value,
    param: start: end value, e.g 1.2990, 99.887
    param: decimal: lenght of float value, default is 5
    """
    return round(random.uniform(start, end), decimal)


def get_random_int(start=1, end=99) -> int:
    """Generate random integer value"""
    return random.randint(start, end)


def get_tree_specs() -> namedtuple:
    """returns random tree specs from tree specs disctionary, like
        common name, botanical name, speci code etc

    Returns:
        namedtouple
    """
    tree_specs = namedtuple("tree_specs", ["common_name", "scientific_name", "specie_code"])
    common_name, scientific_name = random.choice(list(const.specie_names.items()))
    specie_code = const.specie_codes.get(common_name)

    return tree_specs(common_name=common_name, scientific_name=scientific_name, specie_code=specie_code)
