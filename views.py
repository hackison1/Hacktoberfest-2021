from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    HttpResponse,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import AccountAuthenticationForm, CustomerCreationForm, SubscriptionForm
from .models import Account, Customer, Subscription
from django.utils.timezone import now
import datetime
import calendar

EXPIRED_USER = "expired"
PENDING_USER = "pending"
ACTIVE_USER = "active"
CURRENT_DATE = now().strftime("%Y-%m-%d")


def generate_balance(subs):
    current_balance = 0
    balance = []
    for sub in subs:
        if sub["debit_amount"] != 0:
            current_balance += sub["debit_amount"]
        else:
            if current_balance - sub["credit_amount"] > 0:
                current_balance = current_balance - sub["credit_amount"]
            else:
                current_balance = 0
        balance.append(current_balance)
    return balance


def generate_expire_date(subs):
    current_date = now().strftime("%Y-%m-%d")
    expire_dates = []
    first_sub = True
    expired_date = None
    for sub in subs:
        initial_date = sub["sub_date"]
        package = sub["package"]
        if first_sub:
            expired_date = initial_date + datetime.timedelta(days=package * 30)
            first_sub = False
        else:
            if initial_date.strftime("%Y-%m-%d") < expired_date.strftime("%Y-%m-%d"):
                expired_date = expired_date + datetime.timedelta(days=package * 30)
            else:
                expired_date = initial_date + datetime.timedelta(days=package * 30)
        expire_dates.append(expired_date)
    return expire_dates


def save_subs(request, form, customer):
    p_t = int(form.cleaned_data["package"])  # package
    credit_debit_radio = form.cleaned_data["debit_or_credit_radio"]
    amount = form.cleaned_data["amount"]
    subs = form.save(commit=False)  # subscription object
    customer.activation = ACTIVE_USER
    subs.credit_amount = 0
    subs.debit_amount = 0
    if credit_debit_radio == "D":
        subs.debit_amount = amount
    else:
        subs.credit_amount = amount
    subs.customer = customer
    subs.package = p_t
    subs.save()
    customer.save()  # save in customer table


def main(request):
    return render(request, "dashboard/index.html")


def handle404(request, exception):
    return render(request, "dashboard/400.html", status=404)


def handler500(request):
    return render(request, "dashboard/500.html", status=500)


@login_required(login_url="/login")
def dashboard_view(request):
    context = {}
    customers = Customer.objects.filter(user=request.user)
    active_users = Customer.objects.filter(activation=ACTIVE_USER,user=request.user)
    pending_users = Customer.objects.filter(activation=PENDING_USER,user=request.user)
    expired_users = Customer.objects.filter(activation=EXPIRED_USER,user=request.user)
    context["customers"] = customers
    context["active_users"] = active_users
    context["pending_users"] = pending_users
    context["expired_users"] = expired_users
    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="/login")
def customer_view(request):
    context = {}
    customers = Customer.objects.filter(user=request.user)
    context["customers"] = customers
    return render(request, "dashboard/customers.html", context)


@login_required(login_url="/login")
def staff_view(request):

    return render(request, "dashboard/staff.html")


@login_required(login_url="/login")
def customer_profile_view(request, customer_id):
    context = {}
    customer = get_object_or_404(
        Customer.objects.all(), user=request.user, pk=customer_id
    )
    subs = Subscription.objects.filter(customer=customer)
    balance = generate_balance(subs.values())
    exp_dates = generate_expire_date(subs.values())
    current_exp_date = customer.exp_date.strftime("%Y-%m-%d")
    if len(subs) > 0:
        if current_exp_date != exp_dates[-1].strftime("%Y-%m-%d"):
            customer.exp_date = exp_dates[-1]
            customer.save()
    context["customer"] = customer
    context["subs"] = zip(balance, subs, exp_dates)
    return render(request, "dashboard/customer_profile.html", context)


@login_required(login_url="/login")
def customer_subscription_view(request, customer_id):
    context = {}
    customer = get_object_or_404(
        Customer.objects.all(), user=request.user, pk=customer_id
    )
    context["customer"] = customer
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            save_subs(request, form, customer)
            return redirect(reverse("customer_profile", args=[customer_id]))
    else:
        initial_date = now().strftime("%Y-%m-%d")
        form = SubscriptionForm(initial={"sub_date": initial_date})
    context["form"] = form
    return render(request, "dashboard/add-subscription.html", context)


@login_required(login_url="/login")
def create_customer_view(request):
    context = {}
    if request.POST:
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            # customer.activation = PENDING_USER
            customer.save()
            return redirect(reverse("customer"))

    else:
        form = CustomerCreationForm(initial={"reg_date": CURRENT_DATE})

    context["form"] = form

    return render(request, "dashboard/add-customer.html", context)


def edit_customer_view(request, customer_id):
    context = {}
    context["edit"] = True
    customer = get_object_or_404(Customer, pk=customer_id, user=request.user)
    if request.POST:
        form = CustomerCreationForm(request.POST, instance=customer)
        if form.is_valid():
            name = form.cleaned_data["full_name"]
            address = form.cleaned_data["address"]
            phone = form.cleaned_data["phone"]
            reg_date = form.cleaned_data["reg_date"]
            remarks = form.cleaned_data["remarks"]
            isp = form.cleaned_data["isp"]
            customer = form.save(commit=False)
            customer.name = name
            customer.address = address
            customer.phone = phone
            customer.reg_date = reg_date
            customer.remarks = remarks
            customer.isp = isp
            customer.save()
            return redirect(reverse("customer_profile", args=[customer_id]))
    else:
        form = CustomerCreationForm(instance=customer)

    context["form"] = form
    return render(request, "dashboard/add-customer.html", context)


def edit_subscription_view(request, customer_id, subscription_id):
    context = {}
    customer = get_object_or_404(
        Customer.objects.all(), user=request.user, pk=customer_id
    )
    sub_to_edit = get_object_or_404(Subscription, pk=subscription_id, customer=customer)
    context["customer"] = customer
    context["edit"] = True
    if request.POST:
        form = SubscriptionForm(request.POST, instance=sub_to_edit)
        if form.is_valid():
            save_subs(request, form, customer)
            return redirect(reverse("customer_profile", args=[customer_id]))
    else:
        form = SubscriptionForm(instance=sub_to_edit)

    context["form"] = form
    return render(request, "dashboard/add-subscription.html", context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("dashboard")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                try:
                    redirect_link = request.GET["next"]
                except:
                    redirect_link = "/cms"
                return redirect(redirect_link)

    else:
        form = AccountAuthenticationForm()

    context["form"] = form
    return render(request, "dashboard/login.html", context)


@login_required(login_url="/login")
def profile_view(request):
    context = {}
    user = request.user
    context["user_info"] = user
    return render(request, "dashboard/profile.html", context)


@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="/login")
def delete_user(request, id):
    if request.method == "POST":
        pi = Customer.objects.get(pk=id, user=request.user)
        pi.delete()
        return HttpResponse("{}, deleted!".format(pi.full_name))


@login_required(login_url="/login")
def delete_subscription_view(request, customer_id, subscription_id):
    if request.method == "POST":
        customer = get_object_or_404(
            Customer.objects.all(), user=request.user, pk=customer_id
        )
        pi = get_object_or_404(Subscription, pk=subscription_id, customer=customer)
        pi.delete()
        return HttpResponse("{}, deleted!".format(pi.sub_date))
