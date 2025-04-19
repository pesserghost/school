from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Teacher, Class, Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ClassSerializers(serializers.ModelSerializer):
    class_name = StudentSerializers(many=True)

    class Meta:
        model = Class
        fields = "__all__"

    def create(self, validated_data):
        class_name = validated_data.pop('class_name')
        obj = Class.objects.create(**validated_data)

        for i in class_name:
            Student.objects.create(obj=obj, **i)

        return obj

    def update(self, instance, validated_data):
        class_name = validated_data.pop("class_name", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if class_name is not None:
            instance.tracks.all().delete()
            for class_date in class_name:
                Student.objects.create(album=instance, **class_date)

        return instance


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"