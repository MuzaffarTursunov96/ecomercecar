from rest_framework.views import APIView
from rest_framework.generics import *
from .serializers import *
from rest_framework.response import Response

from .models import Car, CarSpecs

# def CarsAPi(APIView):
#     cars =Car.objects.all()
#     carserializer=CarSerializer(cars,many=True)
#     return Response(carserializer.data)
    
class CarsAPi(APIView):
    def get(self,request):
        print(request.GET.get('is_wishlist'))
        if 'is_wishlist' in request.GET:
            print('helleo')
        cars =Car.objects.all()
        data=[]
        for car in cars:
            carserializer=CarSerializer(car,many=False)
            car_dict=carserializer.data
            spec={}
            wishlist={}
            if CarSpecs.objects.filter(car_id=car.id).exists():
                spec=CarSpecs.objects.get(car_id=car.id)
                spec_serializer=CarSpecSerializer(spec,many=False)
                t=spec_serializer.data
                car_dict['specs']=t
            if WishList.objects.filter(car_id=car.id).exists():
                wishlist=WishList.objects.get(car_id=car.id)
                wishlist_serializer=WishlistSerializer(wishlist,many=False)
                t=wishlist_serializer.data
                car_dict['in_wishlist']=t['like']
            
            data.append(car_dict)
        return Response({'data':data})
    
class CarListAPI(ListAPIView):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
        # return Response({'data':serializer.data})