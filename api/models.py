from django.db import models
from django.urls import reverse





class Student(models.Model):

    Students_gender = (

    ('MALE','Male'),
    ('FEMALE','Female'),
    )
     
    student_fname = models.CharField(max_length=20)
    student_lname = models.CharField(max_length=20)
    student_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length = 13)
    age = models.CharField(max_length = 3)
    date_of_birth = models.DateField( auto_now=False)
    gender = models.CharField(max_length = 12,choices=Students_gender,default='MALE')
    student_img = models.ImageField(max_length=None,upload_to='images',default='/media')
    
    
    
    

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.student_fname + " " + self.student_lname

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})


class Teacher(models.Model):

    Teachers_gender = (

    ('MALE','Male'),
    ('FEMALE','Female'),
    )
     
    teacher_fname = models.CharField(max_length=20)
    teacher_lname = models.CharField(max_length=20)
    tacher_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length = 13)
    age = models.CharField(max_length = 3)
    date_of_birth = models.DateField( auto_now=False)
    gender = models.CharField(max_length=12,choices=Teachers_gender,default='MALE')
    bio = models.TextField(max_length=250)
    teacher_img = models.ImageField(max_length=None,upload_to='images',default='/media')
    
    
    
    

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.teacher_fname + " " + self.teacher_lname

    def get_absolute_url(self):
        return reverse("Teacher_detail", kwargs={"pk": self.pk})


class Course(models.Model):

    course_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    duration = models.DateField(auto_now = False)
    cost = models.CharField(max_length = 50)
    students = models.ManyToManyField(Student, related_name='courses')
    teachers = models.ManyToManyField(Teacher, related_name='courses')


    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

class Enrollment(models.Model):
    date_of_enrollment = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student, related_name='enrollments')
    courses = models.ManyToManyField(Course, related_name='enrollments')
    teachers = models.ManyToManyField(Teacher, related_name='enrollments')
    
    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return ', '.join([str(student) for student in self.students.all()])

    def get_absolute_url(self):
        return reverse("Enrollment_detail", kwargs={"pk": self.pk})

    

class Grade(models.Model):
    Grades = (

    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    )

    grade_value = models.CharField(max_length=1, choices=Grades)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    date = models.DateField( auto_now=False, auto_now_add=False)
    

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

    def __str__(self):
        return self.grade_value

    def get_absolute_url(self):
        return reverse("Grade_detail", kwargs={"pk": self.pk})

