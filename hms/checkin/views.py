from django.shortcuts import render,redirect
from checkin.models import GuestDetails 
from django.http import HttpResponse

# to generate random string for guest_id
import string
import random
N = 7 #length of random string
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
res = str(res)

# Create your views here.
def bookingView(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email'):
                post = GuestDetails()
                post.guest_id = res
                post.name = request.POST.get('name')
                post.email = request.POST.get('email')
                post.ph_no = request.POST.get('phno')
                post.address = request.POST.get('add')
                post.id_proof = request.FILES.get('idp')
                post.room_type = request.POST.get('type')
                post.reservation_status = request.POST.get('status')
                post.checkin = request.POST.get('in_date')
                post.save()
                return render(request, 'booking.html')
            else:
                return render(request,'index.html')


    return render(request, 'index.html')

def display(request):
    gd = GuestDetails.objects.all()


    return render(request,'booking.html',{'gd':gd})

def update(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        no = request.POST.get('phno')
        address = request.POST.get('add')
        room_no = request.POST.get('roomno')
        room_type = request.POST.get('type')
        reservation_status = request.POST.get('status')
        checkin = request.POST.get('in_date')
        checkout = request.POST.get('out_date')

        
        try:
            if GuestDetails.objects.filter(ph_no=no).get(name = name):
                GuestDetails.objects.filter(ph_no=no).update(room_no=room_no)
                GuestDetails.objects.filter(ph_no=no).update(name= name)
                GuestDetails.objects.filter(ph_no=no).update(room_type=room_type)
                GuestDetails.objects.filter(ph_no=no).update(email=email)
                GuestDetails.objects.filter(ph_no=no).update(checkin=checkin)
                GuestDetails.objects.filter(ph_no=no).update(checkout=checkout)
                GuestDetails.objects.filter(ph_no=no).update(reservation_status=reservation_status)
                GuestDetails.objects.filter(ph_no=no).update(address=address)


                return HttpResponse("<h1>Success</h1>")
        except:
            pass
    else:
        return render(request,'update1.html')

def delete(request):
    if request.method == 'POST':
        no = request.POST.get('phno')
        if request.POST.get('name') and request.POST.get('phno'):
            gdu = GuestDetails.objects.filter(ph_no = no)
            gdu.delete()
            

    

    return render(request,'delete.html')


