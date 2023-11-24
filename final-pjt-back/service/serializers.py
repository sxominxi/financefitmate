from rest_framework import serializers
from .models import DepositOptions, DepositProducts, InstallmentProducts, InstallmentOptions

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class DepositProductsSerializer(serializers.ModelSerializer):
    option_set = DepositOptionsSerializer(many=True, read_only=True, source='depositoptions_set')

    class Meta():
        model = DepositProducts
        fields = '__all__'


class InstallmentOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = InstallmentOptions
        fields = '__all__'
        read_only_fields = ('product',)


class InstallmentProductsSerializer(serializers.ModelSerializer):
    option_set = InstallmentOptionsSerializer(many=True, read_only=True, source='installmentoptions_set')

    class Meta():
        model = InstallmentProducts
        fields = '__all__'

