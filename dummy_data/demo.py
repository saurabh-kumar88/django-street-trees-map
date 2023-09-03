import json


def read_json_db():
    with open("dummy_data/rk_ashram_dummy_data.json", "r") as f:
        data = json.loads(f.read())
    return data


def get_all_columns(data_dict: dict, column_name: str):
    if not (column_name and isinstance(column_name, str)):
        raise ValueError(f"Invalid input - {column_name!r}")

    columns_data = []

    for k, v in data_dict.items():
        columns_data.append(data_dict[k].get(column_name))
    return columns_data


def search_tree_by_code(data_dict: dict, tree_code: str):
    if not (tree_code and isinstance(tree_code, str)):
        raise ValueError(f"Invaled inputs - {tree_code!r}")
    return data_dict.get(tree_code, f"Tree code {tree_code!r} not  found")


if __name__ == "__main__":
    tree_code = "rk_mq3089w0"
    data = read_json_db()

    # print(get_all_columns(data_dict=data, column_name='common_name'))
    print(search_tree_by_code(data_dict=data, tree_code="rk_mq3089w0"))
