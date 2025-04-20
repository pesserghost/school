from rest_framework import serializers
from .models import User, Teacher, Student, Class



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'phone_number', 'address', 'photo', 'experience']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cla_ss_string = serializers.StringRelatedField(source='cla_ss')
    cla_ss_pk = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='cla_ss')
    cla_ss_hyperlink = serializers.HyperlinkedRelatedField(
        view_name='class-detail', queryset=Class.objects.all(), source='cla_ss'
    )
    cla_ss_nested = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['user', 'full_name', 'cla_ss_string', 'cla_ss_pk', 'cla_ss_hyperlink', 'cla_ss_nested']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            instance.user.username = user_data.get('username', instance.user.username)
            instance.user.email = user_data.get('email', instance.user.email)
            instance.user.first_name = user_data.get('first_name', instance.user.first_name)
            instance.user.last_name = user_data.get('last_name', instance.user.last_name)
            instance.user.save()

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.save()
        return instance


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['cla_ss']