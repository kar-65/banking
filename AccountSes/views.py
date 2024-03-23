from django.shortcuts import render
from decimal import Decimal
from django.contrib import messages, auth
from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import Transaction
from tkinter import messagebox
# Create your views here.

def deposit(request):
    current_bal = Transaction.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])

        if amount > 0:
            Transaction.objects.create(user=request.user, amount=amount, transct_type='depposit')
            current_bal += amount
            messagebox.showinfo('Balance',f'Deposit Successful. Your current balance is : ${current_bal:.2f}')
            return redirect( '/customerlog')
        else:
            error_msg = "Amount must be greater than zero"
            return render(request, 'deposit.html',{'error_msg': error_msg, 'current_bal': current_bal})
    return render(request, 'deposit.html', {'current_bal': current_bal})

def withdrawal(request):
    current_bal = Transaction.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])
        if 0 < amount <= current_bal:
            Transaction.objects.create(user=request.user, amount=-amount, transct_type='withdrawal')
            current_bal -= amount
            messagebox.showinfo('Balance',f'Withdrawal Successful. Your current balance is : ${current_bal:.2f}')
            # messages.success(request, f'Withdrawal Successful. Your current balance is : ${current_bal:.2f}')
            return redirect('/customerlog')
        else:
            error_msg = "Invalid Withdrawal Amount"
            return render(request, 'withdrawal.html',{'error_msg': error_msg, 'current_bal': current_bal})
    return render(request, 'withdrawal.html', {'current_bal': current_bal})

def balance(request):
    current_bal = Transaction.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    return render(request, 'balance.html', {'current_bal':current_bal})

def logout(request):
    auth.logout(request)
    return redirect('customer')
