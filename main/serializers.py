from rest_framework import serializers
from .models import Class, Student, Teacher


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['cla_ss']


class StudentSerializer(serializers.ModelSerializer):
    # RelatedField lar
    cla_ss_string = serializers.StringRelatedField(source='cla_ss')
    cla_ss_pk = serializers.PrimaryKeyRelatedField(source='cla_ss', queryset=Class.objects.all())
    cla_ss_hyperlink = serializers.HyperlinkedRelatedField(
        source='cla_ss', view_name='class-detail', queryset=Class.objects.all()
    )
    student_url = serializers.HyperlinkedIdentityField(view_name='student-detail')

    # Nested Relationships
    cla_ss_nested = ClassSerializer(source='cla_ss', read_only=True)

    class Meta:
        model = Student
        fields = ['full_name', 'cla_ss_string', 'cla_ss_pk', 'cla_ss_hyperlink', 'student_url', 'cla_ss_nested']

    def create(self, validated_data):
        cla_ss_data = validated_data.pop('cla_ss')
        cla_ss, _ = Class.objects.get_or_create(**cla_ss_data)
        student = Student.objects.create(cla_ss=cla_ss, **validated_data)
        return student

    def update(self, instance, validated_data):
        cla_ss_data = validated_data.pop('cla_ss', None)
        if cla_ss_data:
            cla_ss, _ = Class.objects.get_or_create(**cla_ss_data)
            instance.cla_ss = cla_ss
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.save()
        return instance


class TeacherSerializer(serializers.ModelSerializer):
    cla_ss_string = serializers.StringRelatedField(source='cla_ss', many=True)
    cla_ss_pk = serializers.PrimaryKeyRelatedField(source='cla_ss', many=True, queryset=Class.objects.all())
    cla_ss_hyperlink = serializers.HyperlinkedRelatedField(
        source='cla_ss', view_name='class-detail', many=True, queryset=Class.objects.all()
    )
    teacher_url = serializers.HyperlinkedIdentityField(view_name='teacher-detail')

    # Nested Relationships
    cla_ss_nested = ClassSerializer(source='cla_ss', many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['full_name', 'price', 'cla_ss_string', 'cla_ss_pk', 'cla_ss_hyperlink', 'teacher_url',
                  'cla_ss_nested']

    def create(self, validated_data):
        cla_ss_data = validated_data.pop('cla_ss')
        teacher = Teacher.objects.create(**validated_data)
        for data in cla_ss_data:
            cla_ss, _ = Class.objects.get_or_create(**data)
            teacher.cla_ss.add(cla_ss)
        return teacher

    def update(self, instance, validated_data):
        cla_ss_data = validated_data.pop('cla_ss', None)
        if cla_ss_data:
            instance.cla_ss.clear()
            for data in cla_ss_data:
                cla_ss, _ = Class.objects.get_or_create(**data)
                instance.cla_ss.add(cla_ss)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance