from django import forms

class RecipeForm(forms.Form):
    recipe_message = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"placeholder":"Enter your Recipe", "class":"form-control"}))