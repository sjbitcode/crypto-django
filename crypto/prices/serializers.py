from rest_framework import serializers

from cryptocompare import SUPPORTED_SYMBOLS


class CryptoPairSerializer(serializers.Serializer):

    base = serializers.CharField()
    quote = serializers.CharField()

    def validate_base(self, value):
        value = value.upper()

        if value not in SUPPORTED_SYMBOLS:
            raise serializers.ValidationError("Invalid crypto")

        return value

    def validate_quote(self, value):
        value = value.upper()
        if value not in SUPPORTED_SYMBOLS:
            raise serializers.ValidationError("Invalid crypto")

        return value

    def validate(self, data):
        if data['base'] == data['quote']:
            raise serializers.ValidationError("Base and quote cannot be same")

        return data
