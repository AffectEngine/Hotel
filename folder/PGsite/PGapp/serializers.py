from rest_framework import serializers
from .models import *


class RubricSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = PGSRubric
		fields = "__all__"


class ThingSerializer(serializers.ModelSerializer):
	class Meta:
		model = PGSThing
		fields = "__all__"
