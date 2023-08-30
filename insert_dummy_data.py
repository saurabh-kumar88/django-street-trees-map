import os
import json
import random
import string
import time
import django
from dummy_data import constants as const 
from dummy_data import helper
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from street_trees_app.models import RK_Ashram_marg

def generate_data(lenght=10, road_prefix=""):
    output_data = []
    for _ in range(lenght):
        tree_specs = helper.get_tree_specs()
        output_data.append(
            {
            "Tree_code": helper.get_random_id(prefix=road_prefix),
            "common_name": tree_specs.common_name,
            "scientific_name": tree_specs.scientific_name,
            "Age": helper.get_random_int(5, 99),
            "Height": helper.get_random_float(),
            "Diameter_girth": helper.get_random_float(),
            "closest_address": const.TEST_CLOSEST_ADDRESS,
            "Longitude": helper.get_random_float(28.634727, 28.639328, 6),
            "Latitude": helper.get_random_float(77.205373 ,77.207575, 6),
            "specie_code": tree_specs.specie_code,
            "condition": random.choice(const.TREE_CONDITION)
            }
        )
    return output_data

def write_to_file(file: str="dummy_data/rk_ashram_dummy_data.json", tree_data: list=[]):
    with open(file, "w") as f:
        f.write(json.dumps(tree_data))
    print(f"Data has been written!")

def write_dummy_data_from_file():
    """ write dummy data from local json file to db model
    """
    with open("dummy_data/rk_ashram_dummy_data.json", "r") as file:
        data = json.loads(file.read())

    return data 





if __name__=="__main__":
    
    # tree_data = generate_data(lenght=30, road_prefix="rk")
    # write_to_file(tree_data=tree_data)
    tree_data = write_dummy_data_from_file()
    
    for data in tree_data:
      tree = RK_Ashram_marg(Tree_code=data['Tree_code'],
                            common_name=data['common_name'],
                            scientific_name=data['scientific_name'],
                            Age=data['Age'],
                            Height=data['Height'],
                            Diameter_girth=data['Diameter_girth'],
                            closest_address=data['closest_address'],
                            Longitude=data['Longitude'],
                            Latitude=data['Latitude'],
                            specie_code=data['specie_code'],
                            condition=data['condition'])
      tree.save()
    # print(tree_data)
    print(f"Data inserted successfully !")


# latitude - 77.205373 ,77.207575
# longitude - 28.634727, 28.639328 
    

  
    pass