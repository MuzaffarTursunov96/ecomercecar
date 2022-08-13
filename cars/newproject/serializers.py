from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import *



class CarSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['gasoline', 'steering', 'capacity']
        
        
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['like']
        
class CarSerializer(serializers.ModelSerializer):
    # specs=CarSpecSerializer(many=False)       
    # wishlist =WishlistSerializer(many=False)
    class Meta:
        model = Car
        fields = ['id','name','car_type', 'images','price','discount']
        # depth =1
# class CarSerializer(WritableNestedModelSerializer):
#     specs=CarSpecSerializer(many=False,required=False,source='user_wishlist')       
#     wishlist =WishlistSerializer(many=False,required=False)
#     class Meta:
#         model = Car
#         fields = ['id','name','car_type', 'images', 'specs','wishlist', 'price','discount']
        