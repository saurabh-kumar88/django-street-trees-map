from django import forms

class Search_Tree_By_Code(forms.Form):
  treeCode = forms.CharField(label='Enter 8 digit treeID here', max_length=8)
