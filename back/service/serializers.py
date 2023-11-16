from rest_framework import serializers
from .models import DepositOptions, DepositProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    class DepositOptionsSerializer(serializers.ModelSerializer):
        class Meta():
            model = DepositOptions
            read_only_fields = ('product',)

    class Meta():
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositOptions
        exclude = ('fin_prdt_cd',)
        read_only_fields = ('product',)