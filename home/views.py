from django.shortcuts import render
from .models import Expense, Profile

# Create your views here.
def home(request):
    if request.method == "POST":
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
        print(text)
        print(amount)
        print(expense_type)
    profile = Profile.objects.filter(user=request.user).first()
    context = {"profile": profile}
    print(request.user)
    print(profile)
    print(context)
    return render(request, 'home/home.html',context)