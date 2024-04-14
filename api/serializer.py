from rest_framework import serializers
from .models import Course,Student,Enrollment,Teacher,Grade




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    teachers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Course
        fields = ['id','course_name','description','duration','cost','students','teachers']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"

class EnrollmentListSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(many=True)
    course = serializers.StringRelatedField(many=True)
    teacher = serializers.StringRelatedField(many=True)
    class Meta:
        model = Enrollment
        fields = ['date_of_enrollment','student','course','teacher']

class GradeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Grade
        fields = "__all__"


class GradeListSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(many=False)
    course = serializers.StringRelatedField(many=False)
    class Meta:
        model = Grade
        fields = ['grade_value','date','student','course']

        