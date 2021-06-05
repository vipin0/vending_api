from rest_framework import generics
from api.models import Transaction
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import TransactionSerializer

def getjson(data):
    data = {
        'money':{
            'penny':data['penny'],
            'nickel':data['nickel'],
            'dime':data['dime'],
            'quarter':data['quarter'],
            'total':data['total'],
            'balance':data['balance'],
        },
        'purchased items':{
            'coke':data['coke'],
            'pepsi':data['pepsi'],
            'soda':data['soda'],
            'order':{
                'coke':"%s x 25"%data['coke'],
                'pepsi':"%s x 32"%data['pepsi'],
                'soda':"%s x 47"%data['soda'],
                'billed':data['total']-data['balance'],
                'balance':data['balance']
            }
        },
        'timestamp': data['timestamp']
    }
    return data
@api_view(['POST'])
def order(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            total = int(data.get('penny',0))+int(data.get('nickel',0))*5+int(data.get('dime',0))*10+int(data.get('quarter',0))*25
            purchased = int(data.get('coke',0))*25+int(data.get('pepse',0))*32+int(data.get('soda',0))*47
            balance=total-purchased
            if(total<purchased):
                msg = {
                    'error':"Not enough money to purchage !"
                }
                return JsonResponse(msg,safe=False)
            serializer.save(total=total,balance=balance)
            return JsonResponse(getjson(serializer.data),status=201,safe=False)
        return JsonResponse(serializer.errors,status=400)

# @api_view(['GET'])
# def orders(request):
#     # serialized_obj = serializers.serialize('json', Transaction.objects.all())
#     return Response(Transaction.objects.all())

class OrderList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# class OrderLists(generics.CreateAPIView,generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)

class CreateOrder(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer