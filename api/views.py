from rest_framework import generics,permissions
from .models import Course,Student,Teacher,Enrollment,Grade 
from .serializer import CourseSerializer,StudentSerializer,TeacherSerializer,EnrollmentSerializer,  EnrollmentListSerializer,GradeSerializer, GradeListSerializer,CourseListSerializer
 
1
class CourseApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = (permissions.AllowAny,)

class CourseCreateApiView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAdminUser,)

class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny,)


class CourseUpdateApiView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAdminUser,)

class CourseDeleteApiView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAdminUser,)

2

class StudentApiView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny,)

class StudentCreateApiView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAdminUser,)

class StudentDetailApiView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny,)

class StudentUpdateApiView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAdminUser,)

class StudentDeleteApiView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAdminUser,)

3


class TeacherApiView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.AllowAny,)

class TeacherCreateApiView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class =TeacherSerializer
    permission_classes = (permissions.IsAdminUser,)

class TeacherDetailApiView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.AllowAny,)

class TeacherUpdateApiView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAdminUser,)

class TeacherDeleteApiView(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAdminUser,)

4


class EnrollmentApiView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentListSerializer
    permission_classes = (permissions.AllowAny,)

class EnrollmentCreateApiView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAdminUser,)

class EnrollmentDetailApiView(generics.RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.AllowAny,)

class EnrollmentUpdateApiView(generics.UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAdminUser,)

class EnrollmentDeleteApiView(generics.DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAdminUser,)

5

class GradeApiView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeListSerializer
    permission_classes = (permissions.AllowAny,)

class GradeCreateApiView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAdminUser,)

class GradeDetailApiView(generics.RetrieveAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.AllowAny,)

class GradeUpdateApiView(generics.UpdateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAdminUser,)

class GradeDeleteApiView(generics.DestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAdminUser,)