import socket

from django.shortcuts import render, redirect
from json import dumps

from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound, HttpRequest
from django.contrib import messages
from django.conf import settings
from django.template import RequestContext


from .forms import Search_Tree_By_Code
from .models import RK_Ashram_marg


# Create your views here.

def home(request):
  if request.user.is_superuser:
    return redirect("shaasan-prabandhan-page/")

  return render( request, "home/home.html")

def render_map(request):
  Tree_Codes = RK_Ashram_marg.objects.values('Tree_code')
  Common_names = RK_Ashram_marg.objects.values('common_name')
  Longitude = RK_Ashram_marg.objects.values('Longitude')
  Latitude = RK_Ashram_marg.objects.values('Latitude')

  tree_codes = []
  for codes in Tree_Codes:
    tree_codes.append(codes['Tree_code'])
  
  common_names = []
  for names in Common_names:
    common_names.append(names['common_name'])
  
  longitudes = []
  latitudes = []
  
  for x in Longitude:
    longitudes.append(str(x['Longitude']))
    
  for x in Latitude:
    latitudes.append(str(x['Latitude']))
  
    
  JSON_tree_codes = dumps(tree_codes)
  JSON_common_names = dumps(common_names)
  JSON_longitudes = dumps(longitudes)
  JSON_latitudes = dumps(latitudes)

  context = {'Tree_Codes'    : JSON_tree_codes,
              'Common_names' : JSON_common_names,        
              'Longitudes'    : JSON_longitudes,
              'Latitudes'    : JSON_latitudes,
               }
  return render(request, "map/map.html", context=context)


def search_tree(request):
  
  if request.method == 'POST':
    form = Search_Tree_By_Code(request.POST)
    if form.is_valid():
      
      requested_tree_code = form.cleaned_data.get('treeCode')
      treeInfo = RK_Ashram_marg.objects.all().filter(Tree_code=requested_tree_code)
      
      if(len(treeInfo) != 0):
        # request database call
        context = {}
        for data in treeInfo:
          context['common_name'] = data.common_name
          context['botanicalName'] = data.scientific_name

        context["treeInfo"] = treeInfo
          
        return render(request, 'street_trees/tree_view.html', context=context)
      else:
        form = Search_Tree_By_Code()
        messages.info(request, f'Invalid Tree Code!')
        return render(request, 'street_trees/search_tree.html', {'form' : form})
        
  else:
    form = Search_Tree_By_Code()
    return render(request, 'street_trees/search_tree.html', {'form' : form})


  
def get_tree_info(request):
  
  if request.method == 'GET':
    requested_tree_code = request.GET['ID']
    
    # request database call
    treeInfo = RK_Ashram_marg.objects.all().filter(Tree_code=requested_tree_code)
     
    context = {}
    for data in treeInfo:
      context['common_name'] = data.common_name
      context['botanicalName'] = data.scientific_name
  

    context["treeInfo"] = treeInfo
    
    
    return render(request, 'street_trees/tree_view.html', context=context)

  


# --------------- static pages ---------------

def DosAndDonts(request):
  return render(request, "DosAndDonts/DosAndDonts.html")

def whyStreetTrees(request):
  return render(request, "whyStreetTrees/whyStreetTrees.html")  

def developer(request):
  return render(request, "developer/developer.html")


#---------------- Custom views to Handle bad requests -------------

def page_not_found_handler(request, *args, **argv):
    context = {"status_code" : 404,
                "error_message" : "Page Not Found"}
    return render(request, '404.html',context=context)


def server_error_handler(request, *args, **argv):
    context = {"status_code" : 500,
                "error_message" : "Sorry, server error."}
    return render(request, 'httpError.html', context=context)


def permission_denied_handler(request, *args, **argv):
    context = {"status_code" : 403,
                "error_message" : "Bad request!"}
    return render(request, 'httpError.html', context=context)

def bad_request_handler(request, *args, **argv):
    context = {"status_code" : 400,
                "error_message" : "Forbidden."}
    return render(request, 'httpError.html', context=context)


  


