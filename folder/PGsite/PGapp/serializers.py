import io
from abc import ABC

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


# class RubricModel:
# 	def __init__(self, rubric, description, tags):
# 		self.rubric = rubric
# 		self.description = description
# 		self.tags = tags


class RubricSerializer(serializers.ModelSerializer):
	class Meta:
		model = PGSRubric
		fields = "__all__"


# def encode():
# 	model = RubricModel('Rub35', 'Desc!', ['tag1', 'tag2', 'tag3'])
# 	model_sr = RubricSerializer(model)
# 	print(model_sr.data, type(model_sr.data), sep='\n')
# 	json = JSONRenderer().render(model_sr.data)
# 	print(json)


# def decode():
# 	stream = io.BytesIO(b'{"rubric":"Rub3Dec", "description":"Desc3Dec", "tags":["tag1","tag2","tag3"]}')
# 	data = JSONParser().parse(stream)
# 	serializer = RubricSerializer(data=data)
# 	serializer.is_valid()
# 	print(serializer.validated_data)


