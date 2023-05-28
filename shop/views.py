from django.shortcuts import render,redirect
from shop import models
from rest_framework import viewsets
from shop.models import Shoe
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from shop.serializers import ShoeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe
from django.urls import reverse
from django.http import JsonResponse
from paypal.standard.forms import PayPalPaymentsForm
stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, 'index.html')

def payment(request):
    # عرض نموذج الدفع
    return render(request, 'payment.html')
def payment_success(request):
    return render(request,'payment_success.html')
    
def payment_error(request):
    return render(request, 'payment_error.html')


def payment(request):
    # تعريف بيانات الدفع
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '10.00',
        'currency_code': 'USD',
        'item_name': 'Product Name',
        'invoice': 'unique-invoice-id',
        'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
        'return_url': request.build_absolute_uri(reverse('payment_success')),
        'cancel_return': request.build_absolute_uri(reverse('payment_error')),
    }

    # إنشاء نموذج دفع PayPal
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form}
    return render(request, 'payment.html', context)
    
# def payment(request):
#     # تعريف بيانات الدفع
#     paypal_dict = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': '10.00',}



def create_payment_intent(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
            )
            client_secret = intent.client_secret
            return JsonResponse({'client_secret': client_secret})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})

    # else:
    #     # في حالة استلام طلب GET، يجب إعادة التوجيه إلى صفحة الدفع
    #     return redirect('home')
# # Create your views here.
# class Shoeviews(viewsets.ModelViewSet):
#     queryset = Shoe.objects.all()
#     serializer_class = ShoeSerializer


def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)



def search(request):
    if request.method=='GET':
        date = models.search.objects.all()
        context = {'date': date }
    return render(request, 'search.html', context)

def Shoe_list(request):
    product = None

    if request.method=='GET': 
        product = Shoe.objects.filter(Q(name__iregex=request.GET.get('search'))).all()

    return render(request, 'shoe.html',{
        'Shoe':product,
    })



def add_shoe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        color = request.POST.get('color')
        size=request.POST.get('size')
        price=request.POST.get('price')
        image=request.POST.get('image')
        Shoe.objects.create(name=name, brand=brand, color=color, size=size, price=price, image=image) # إنشاء الحذاء في قاعدة البيانات
        return redirect('shoe_list')
    else:
        shoes = Shoe.objects.all() 
        return render(request, 'add_shoe.html', {'shoes': shoes})




@api_view(['POST']) 
def apiApplication(request):
      Shoe.objects.create(
            name=request.POST['name'],
            brand=request.POST['brand'],
            color=request.POST['color'],
            size=request.POST['size'],
            price=request.POST['price'],
            image=request.FILES['image'],
      )

      return Response({
            'message': 'shoes has been added successfully',
            'status':200
      })



























