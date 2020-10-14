from django.shortcuts import render, HttpResponse
from django.views import generic
# from rest_framework import generics
# from .serializers import OrderSerializer
from .models import Orders

# Create your views here.

def order(request):
    return render(request, "order.html", {})

class HomePage(generic.View):

    def get(self, *args, **kwargs):

        context = {

        }


        return render(self.request, "index.html", context)

    def post(self, *args, **kwargs):
        pass

class OrderUpload(generic.CreateView):
    model = Orders
    fields = ["topic", "pages", "style", "subject", "amount", "instructions", "uploads"]
    template_name = "order_Upload.html"


# class OrderList(generics.ListCreateAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrderSerializer


# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrderSerializer

