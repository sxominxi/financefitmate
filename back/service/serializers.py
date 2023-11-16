from rest_framework import serializers
from .models import DepositOptions, DepositProducts, InstallmentProducts, InstallmentOptions

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


class InstallmentProductsSerializer(serializers.ModelSerializer):
    class InstallmentOptionsSerializer(serializers.ModelSerializer):
        class Meta():
            model = InstallmentOptions
            read_only_fields = ('product',)

    class Meta():
        model = InstallmentProducts
        fields = '__all__'

class InstallmentOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = InstallmentOptions
        exclude = ('fin_prdt_cd',)
        read_only_fields = ('product',)