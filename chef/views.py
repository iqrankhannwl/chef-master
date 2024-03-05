from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from .form import RecipeForm
class HomeView(View):
    def get(self, request):
        form  = RecipeForm()
        return render(request, "chef/home.html", {"form":form})
    
    def post(self,request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data["recipe_message"]
            print(recipe_message)
        form = RecipeForm()
        return redirect("/")
