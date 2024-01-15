from django.shortcuts import render, redirect
from .models import Expense, Profile

# Create your views here.
def home(request):
    profile = Profile.objects.get(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    if request.method == "POST":
        text = request.POST.get('text')
        amount = int(request.POST.get('amount'))
        expense_type = request.POST.get('expense_type')
        
        expense = Expense(name=text, amount=amount,user=request.user, expense_type=expense_type)
        expense.save()
        if expense_type == "Positive":
            profile.balance += amount
        else:
            profile.balance -= amount
            profile.expenses += amount
            
        
        profile.save()
        return redirect("/")
        
    context = {"profile": profile,"expenses": expenses}
    print(request.user)
    print(profile)
    print(context)
    return render(request, 'home/home.html',context)