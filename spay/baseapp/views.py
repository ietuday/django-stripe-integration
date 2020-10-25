from django.shortcuts import render,redirect
from django.urls import reverse
import stripe
# Create your views here.
stripe.api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'




def home(request):
    context = {}
    return render(request,'template.html',context)


def charge(request):
    if request.method == 'POST':

        amount = request.POST['amount']
        print("amount",amount)
        print("amount",request.POST)
        customer =  stripe.Customer.create(
        name = request.POST['name'],
        email= request.POST['email'],
        source = request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
        customer =customer,
        amount = int(request.POST['amount'])*100,
        currency="inr",
        description = 'Dontation'
        )

    return redirect(reverse('success',args=[amount]))


def success(request,args):
    amount = args
    context = {'amount':amount}

    return render(request,'success.html',context)
