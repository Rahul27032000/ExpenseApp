from django.shortcuts import render
from .models import Expense, Profile

# Create your views here.
def home(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        text = request.POST.get('text')
        amount = int(request.POST.get('amount'))
        expense_type = request.POST.get('expense_type')
        
        
        if expense_type == "Positive":
            profile.balance += amount
        else:
            profile.balance -= amount
            profile.expenses += amount
            
        
        profile.save()
        
    context = {"profile": profile}
    print(request.user)
    print(profile)
    print(context)
    return render(request, 'home/home.html',context)