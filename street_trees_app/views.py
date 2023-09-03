import json
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Search_Tree_By_Code
from .models import RK_Ashram_marg


# Create your views here.

LOCAL_DATA_FILE_PATH = "dummy_data/rk_ashram_dummy_data.json"
with open(LOCAL_DATA_FILE_PATH, "r") as file:
    LOCAL_DATA = json.loads(file.read())

# utility functions to simulate db actions

# def read_json_db():
#     with open("dummy_data/rk_ashram_dummy_data.json", "r") as f:
#         data = (json.loads(f.read()))
#     return data


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


def home(request):
    if request.user.is_superuser:
        return redirect("shaasan-prabandhan-page/")

    return render(request, "home/home.html")


def render_map(request):
    # Tree_Codes = RK_Ashram_marg.objects.values('Tree_code')
    # Common_names = RK_Ashram_marg.objects.values('common_name')
    # Longitude = RK_Ashram_marg.objects.values('Longitude')
    # Latitude = RK_Ashram_marg.objects.values('Latitude')

    Tree_Codes = get_all_columns(data_dict=LOCAL_DATA, column_name="Tree_code")
    Common_names = get_all_columns(data_dict=LOCAL_DATA, column_name="common_name")
    Longitudes = get_all_columns(data_dict=LOCAL_DATA, column_name="Longitude")
    Latitudes = get_all_columns(data_dict=LOCAL_DATA, column_name="Latitude")

    # tree_codes = []
    # for codes in Tree_Codes:
    #   tree_codes.append(codes['Tree_code'])

    # common_names = []
    # for names in Common_names:
    #   common_names.append(names['common_name'])

    # longitudes = []
    # latitudes = []

    # for x in Longitude:
    #   longitudes.append(str(x['Longitude']))

    # for x in Latitude:
    #   latitudes.append(str(x['Latitude']))

    JSON_tree_codes = json.dumps(Tree_Codes)
    JSON_common_names = json.dumps(Common_names)
    JSON_longitudes = json.dumps(Longitudes)
    JSON_latitudes = json.dumps(Latitudes)
    JSON_host_name = json.dumps(str(request.get_host()))

    context = {
        "Tree_Codes": JSON_tree_codes,
        "Common_names": JSON_common_names,
        "Longitudes": JSON_longitudes,
        "Latitudes": JSON_latitudes,
        "host_name": JSON_host_name,
    }
    return render(request, "map/map.html", context=context)


def search_tree(request):
    if request.method == "POST":
        form = Search_Tree_By_Code(request.POST)
        if form.is_valid():
            requested_tree_code = form.cleaned_data.get("treeCode")
            # treeInfo = RK_Ashram_marg.objects.all().filter(Tree_code=requested_tree_code)
            treeInfo = search_tree_by_code(data_dict=LOCAL_DATA, tree_code=requested_tree_code)

            if len(treeInfo) != 0:
                # request database call
                context = {}
                # for data in treeInfo:
                #   context['common_name'] = data.common_name
                #   context['botanicalName'] = data.scientific_name
                context["common_name"] = treeInfo.get("common_name")
                context["botanicalName"] = treeInfo.get("scientific_name")

                context["treeInfo"] = treeInfo

                return render(request, "street_trees/tree_view.html", context=context)
            else:
                form = Search_Tree_By_Code()
                messages.info(request, f"Invalid Tree Code!")
                return render(request, "street_trees/search_tree.html", {"form": form})

    else:
        form = Search_Tree_By_Code()
        return render(request, "street_trees/search_tree.html", {"form": form})


def get_tree_info(request):
    if request.method == "GET":
        requested_tree_code = request.GET["ID"]

        # request database call
        # treeInfo = RK_Ashram_marg.objects.all().filter(Tree_code=requested_tree_code)
        treeInfo = search_tree_by_code(data_dict=LOCAL_DATA, tree_code=requested_tree_code)

        context = {}
        # for data in treeInfo:
        #   context['common_name'] = data.common_name
        #   context['botanicalName'] = data.scientific_name

        context["common_name"] = treeInfo.get("common_name")
        context["botanicalName"] = treeInfo.get("data.scientific_name")

        context["treeInfo"] = treeInfo

        return render(request, "street_trees/tree_view.html", context=context)


# --------------- static pages ---------------


def DosAndDonts(request):
    return render(request, "DosAndDonts/DosAndDonts.html")


def whyStreetTrees(request):
    return render(request, "whyStreetTrees/whyStreetTrees.html")


def developer(request):
    return render(request, "developer/developer.html")


# ---------------- Custom views to Handle bad requests -------------


def page_not_found_handler(request, *args, **argv):
    context = {"status_code": 404, "error_message": "Page Not Found"}
    return render(request, "404.html", context=context)


def server_error_handler(request, *args, **argv):
    context = {"status_code": 500, "error_message": "Sorry, server error."}
    return render(request, "httpError.html", context=context)


def permission_denied_handler(request, *args, **argv):
    context = {"status_code": 403, "error_message": "Bad request!"}
    return render(request, "httpError.html", context=context)


def bad_request_handler(request, *args, **argv):
    context = {"status_code": 400, "error_message": "Forbidden."}
    return render(request, "httpError.html", context=context)
