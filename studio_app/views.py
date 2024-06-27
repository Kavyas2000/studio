from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

import razorpay

from django.utils.crypto import get_random_string
from django.core.mail import send_mail

# Create your views here.

# <!-----------------------HOME PAGE---------------------------!>


def index(req):
    return render(req,'index.html')
def admin_contact(req):
    data=contact.objects.all()
    return render(req,'admin_contact.html',{'data':data})

def admin_feedback(req):
    data=feedback.objects.all()
    return render(req,'admin_feedback.html',{'data':data})

def contact_fu(req):
    if req.method == 'POST':
        n = req.POST['name']
        p= req.POST['phone']
        e = req.POST['email']
        m = req.POST['message']
        details = contact.objects.create(name=n,phone=p,email=e,message=m)
        details.save()
        messages.info(req, "Contact send Successfully")
    return render(req,'contact.html')
def portfolio(req):
    return render(req,'portfolio.html')
def about(req):
    return render(req,'about.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['u_name']
        p1 = request.POST['pass']
        # try:
        user = auth.authenticate(username=un, password=p1)
        # try:
        if un=='admin' and p1=='1234':
                    # messages.success(request, 'admin login successfully')
                    request.session['admin'] = un
                    return redirect(admin_index)
        if user is not None:
                    auth.login(request, user)
                    request.session['usr'] = un
                    return redirect(user_index,user.id)

        else:
                    messages.warning(request, 'check credentials again')
                    return redirect(login)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        na = request.POST['name']
        un = request.POST['u_name']
        fn = request.POST['email']
        ph = request.POST['phone']
        p1 = request.POST['pass']
        p2 = request.POST['pass2']
        p = pro(request.POST)

        if (p1 == p2):
            if User.objects.filter(username=un).exists():
                messages.info(request, 'username already exist')
                return redirect(register)

            else:

                user = User.objects.create_user(username=un, last_name=ph,first_name=na,email=fn, password=p1)
                user.save()
                if p.is_valid():
                    pr = p.save(commit=False)
                    pr.u=user
                    pr.save()
                return redirect(login)

        else:
            messages.info(request, 'Invalid passwords')
            return redirect(register)

    return render(request,'register.html')



# <!-----------------------USER PAGE---------------------------!>



def logout_ua(req):
    try:
        logout(req)
        req.session.flush()
    except:
        req.session.flush()
    return redirect(index)


def user_index(req,id):
    data = User.objects.get(pk=id)
    if req.method == 'POST':
        u = req.POST['uname']
        f= req.POST['fname']
        p = req.POST['ph']
        e = req.POST['email']
        User.objects.filter(pk=id).update(username=u,first_name=f,last_name=p,email=e)
        messages.info(req, "Updated Successfully")

    return render(req,'user_index.html',{'data':data})

def user_booking(request):
    if request.method=='POST':
        n=request.POST['name']
        p= request.POST['phone']
        e = request.POST['event']
        o = request.POST['other']
        d = request.POST['date']
        t = request.POST['time']
        pl = request.POST['place']
        s = 'pending'
        m = 'pending'
        a = 0


        details=bookings.objects.create(name=n,phone=p,event=e,other=o,date=d,time=t,place=pl,amount=a,status=s,message=m)
        details.save()
        messages.info(request, "Event Booking Successfully")


    # data = event_booking.objects.filter(user=request.user)
    return render(request,'user_booking.html')



def user_frames(req):
    data = addframe.objects.all()
    return render(req,'user_frames.html', {'data': data})



def user_appoinment(request):

    if request.method=='POST':
        n=request.POST['name']
        p= request.POST['phone']
        e = request.POST['email']
        pur = request.POST['purpose']
        d = request.POST['date']
        t = request.POST['time']
        s = "pending"
        m = "pending"

        details=appoinment.objects.create(user=request.user,name=n,phone=p,email=e,purpose=pur,date=d,time=t,status=s,message=m)
        details.save()
        messages.info(request,"Appoinment book successfully")

    # data = appoinment.objects.filter(user=request.user)
    return render(request,'user_appoinment.html')


def user_design(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['phone']
        e = request.POST['email']
        yo= request.FILES.get('your')
        mo = request.FILES.get('model')
        ex = request.POST['explain']
        s = 'pending'
        me = 'pending'
        a = 0

        details =designs.objects.create(user=request.user,name=n,phone=p,email=e,your=yo,model=mo,explain=ex,amount=a,status=s,message=me)
        details.save()
        # data = des.objects.filter(user=request.user)

        messages.info(request,"Design order successfully")
    return render(request, 'userdesign.html')

def user_feedback(request):
    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['message']

        details =feedback.objects.create(name=n,message=m)
        details.save()
        # data = des.objects.filter(user=request.user)

        messages.info(request,"Feedback send successfully")
        return redirect(user_feedback)
    return render(request, 'user_feedback.html')



def user_logout(req):
    return render(req,'user_logout.html')


# -------------------------------------CART PAGE----------------------------

def view_cart(request):
    cart_items = Cart_Item.objects.filter(user=request.user)
    # data = addframe.objects.get(pk=id)
    # total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'try_cart.html', {'cart_items': cart_items})


def add_to_cart(request,addframe_id):

    name = addframe.objects.get(id=addframe_id)
    cart_item, created = Cart_Item.objects.get_or_create(addframe=name,
                                                        user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(view_cart)


def remove_from_cart(request,item_id):
    cart_item = Cart_Item.objects.get(id=item_id)
    cart_item.delete()
    return redirect(view_cart)

# ********USER_ORDER********
def myproduct(request,id):
    data=addframe.objects.get(pk=id)
    print(data)
    if request.method == 'POST':
        # u = request.POST['username']
        # f=request.POST['frame_name']

        m='pending'
        p = request.POST['phone']
        e = request.POST['email']
        i = request.FILES.get('img')

        details = frame_orders.objects.create(user=request.user,frame_name=data, phone=p,email =e,img=i, message=m)
        details.save()
        # data =Cart_Item.objects.get(id=id)
        # data.delete()

        messages.info(request, "Order book successfully")
        # return redirect(remove_from_cart)

    # data = frame_order.objects.filter(user=request.user)
    return render(request, 'user_order.html')





# <!-----------------------ADMIN RESPONSE IN USER SIDE---------------------------!>
def status_design(req):
    return render(req,'status_design.html')

# <!-----------------------ADMIN PAGE---------------------------!>

def admin_index(req):
    return render(req,'admin_index.html')
def admin_view_user(req):
    data=User.objects.all()
    return render(req,'admin_view_user.html',{'data':data})


def admin_booking(req,id):
    data = bookings.objects.get(pk=id)
    if req.method=='POST':
        amount = req.POST['amount']
        email=req.POST['e_mail']
        status=req.POST['status']
        message= req.POST['message']
        # send_mail(f'your Event booking is {status}from user {req.user.email}', f'Total amount:{amount},Message:{message}', 'settings.EMAIL_HOST_USER',[email], fail_silently='false')
        bookings.objects.filter(pk=id).update(amount=amount,status=status, message=message)
        return redirect(admin_booking_table)
    return render(req, 'bookingedit.html',{'data':data})
def admin_booking_table(req):
    data = bookings.objects.all()
    return render(req, 'admin_booking.html',{'data':data})







def admin_appoinment_table(req):
    data = appoinment.objects.all()
    return render(req, 'admin_appoinment.html',{'data':data})


def admin_appoinment(req,id):
    data = appoinment.objects.get(pk=id)
    if req.method=='POST':
        email=req.POST['email']
        status=req.POST['status']
        message = req.POST['message']
        send_mail(f'your appoinment booking is {status}from user {req.user.email}', f'Message:{message}', 'settings.EMAIL_HOST_USER',[email], fail_silently='false')
        # event_booking.objects.filter(pk=id).update(status=status, message=message)
        appoinment.objects.filter(pk=id).update(status=status,message=message)
        return redirect(admin_appoinment_table)

    return render(req, 'appoinmentedit.html',{'data':data})




def admin_design(req):
    data = designs.objects.all()
    return render(req,'admin_design.html', {'data': data})

def admin_designstatus(req,id):
    data =designs.objects.get(pk=id)
    if req.method=='POST':
        amount= req.POST['amount']
        email=req.POST['email']
        status=req.POST['status']
        message = req.POST['message']
        send_mail(f'your Design is {status}from user {req.user.email}', f'Amount:{amount},Message{message}', 'settings.EMAIL_HOST_USER',[email], fail_silently='false')
        designs.objects.filter(pk=id).update(amount=amount,status=status,message=message)
        return redirect(admin_design)
    return render(req, 'designedit.html',{'data':data})

def displaygallery(req):
    data = gallery.objects.all()
    return render(req, 'displaygallery.html', {'data': data})
def admin_gallery(r):
    pobj = galleryform()
    if r.method == 'POST':
        pobj1 = galleryform(r.POST, r.FILES)
        if pobj1.is_valid():
            pobj1.save()
            messages.info(r, "Image Inserted")
            # return redirect(displaygallery)
    return render(r, 'admin_gallery.html', {'form': pobj})



def admin_addframe(r):
    pobj = addform()
    if r.method == 'POST':
        pobj1 = addform(r.POST, r.FILES)
        if pobj1.is_valid():
            pobj1.save()
            return redirect(admin_displayframes)
    return render(r, 'admin_addframe.html', {'form': pobj})
def admin_displayframes(req):
    data = addframe.objects.all()
    return render(req,'admin_displayframes.html', {'data': data})
def admin_frameedit(r,id):
    prd1 = addframe.objects.get(pk=id)
    pobj = addform(instance=prd1)
    if r.method == 'POST':
        pobj1 = addform(r.POST,r.FILES,instance=prd1)
        if pobj1.is_valid():
            pobj1.save()
        return redirect(admin_displayframes)
    return render(r,'admin_frameedit.html',{'form':pobj})
# **********FRAME DELETE****************

def admin_framedelete(reg,id):
    data = addframe.objects.get(id=id)
    data.delete()
    return redirect(admin_displayframes)




def admin_order(req):
    data = frame_orders.objects.all()
    return render(req,'admin_order.html', {'data': data})
def admin_orderstatus(req,id):
    data = frame_orders.objects.get(pk=id)
    if req.method == 'POST':
        email=req.POST['e_mail']
        # status = req.POST['status']
        message = req.POST['message']
        send_mail(f'your Order is get from user {req.user.email}', f'Message:{message}', 'settings.EMAIL_HOST_USER',[email], fail_silently='false')
        frame_orders.objects.filter(pk=id).update(message=message)
        return redirect(admin_order)

    return render(req, 'admin_orderstatus.html', {'data': data})



# <!-----------------------FORGOT PASSWORD---------------------------!>

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forgot_password.html')


def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.set_password(new_password)
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'reset_password.html',{'token':token})



# <!-----------------------RESPONSE PAGE---------------------------!>





def response_booking(request):
    data=bookings.objects.all()
    data =bookings.objects.filter(name=request.user)
    return render(request, 'response_booking.html', {'data': data})
def response_appoinment(request):
    data=appoinment.objects.all()
    data =appoinment.objects.filter(name=request.user)
    return render(request, 'response_appoinment.html', {'data': data})
def response_design(request):
    data=designs.objects.all()
    data =designs.objects.filter(name=request.user)
    return render(request, 'response_design.html', {'data': data})

def response_order(request):
    data=frame_orders.objects.all()
    data =frame_orders.objects.filter(user=request.user)
    return render(request, 'response_order.html', {'data': data})

def payment_message(request):
    return render(request,'payment_status.html')

def payment(request,id,amount):
    data = bookings.objects.get(id=id)
    amount =amount*100
    if amount==0:
        messages.info(request, "Payment in pending state....")
        return render(request, 'payment_status.html', {'data': data})


    order_currency = 'INR'
    client = razorpay.Client(
    auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

    # cursor = connection.cursor()
    # cursor.execute(
    #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
    #         id) + "' ")


    payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    # messages.info(request, "Payment done successfully....")
    return render(request, "payment.html",{'payment':payment,'id':id})

def success_booking(request,id):
    data = bookings.objects.get(id=id)
    p="paid"
    bookings.objects.filter(pk=id).update(payment_status=p)
    # data.payment_status=p
    messages.info(request, 'Paid Successfully...')
    return render(request,'payment_status.html',{'data':data})



def payment_order(request,id,amount):
    data =frame_orders.objects.get(id=id)
    amount =amount*100
    if amount==0:
        messages.info(request, "Payment in pending state....")
        return render(request, 'payment_status.html', {'data': data})


    order_currency = 'INR'
    client = razorpay.Client(
    auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

    # cursor = connection.cursor()
    # cursor.execute(
    #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
    #         id) + "' ")


    payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    # messages.info(request, "Payment done successfully....")
    return render(request, "payment_order.html",{'payment':payment,'id':id})


def success_order(request,id):
    data = frame_orders.objects.get(id=id)
    p="paid"
    frame_orders.objects.filter(pk=id).update(payment_status=p)
    # data.payment_status=p
    messages.info(request, 'Paid Successfully...')
    return render(request,'payment_status.html',{'data':data})


def payment_design(request,id,amount):
    data =designs.objects.get(id=id)
    amount =amount*100
    if amount==0:
        messages.info(request, "Payment in pending state....")
        return render(request, 'payment_status.html', {'data': data})


    order_currency = 'INR'
    client = razorpay.Client(
    auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

    # cursor = connection.cursor()
    # cursor.execute(
    #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
    #         id) + "' ")


    payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    # messages.info(request, "Payment done successfully....")
    return render(request, "payment_design.html",{'payment':payment,'id':id})


def success_design(request,id):
    data = designs.objects.get(id=id)
    p="paid"
    designs.objects.filter(pk=id).update(payment_status=p)
    # data.payment_status=p
    messages.info(request, 'Paid Successfully...')
    return render(request,'payment_status.html',{'data':data})
