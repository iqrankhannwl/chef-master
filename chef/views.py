from django.shortcuts import render, redirect
from django.views import View
from .langchan import chef_model
# Create your views here.
from .form import RecipeForm
class HomeView(View):
    def get(self, request):
        response = request.session.get("recipe", "")
        form  = RecipeForm()
        return render(request, "chef/home.html", {"form":form, "response":response})
    
    def post(self,request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data["recipe_message"]
            model_responce=chef_model(recipe_message)
            request.session["recipe"] = model_responce
        form = RecipeForm()
        return redirect("/")
