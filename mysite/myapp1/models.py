from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class address(models.Model):
    name=models.OneToOneField(student,on_delete=models.CASCADE)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)

class skill(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class candidate(models.Model):
    name=models.CharField(max_length=50)
    title=models.ManyToManyField(skill)
    def __str__(self):
        return self.name


class author(models.Model):
    name=models.CharField(max_length=50)
    def  __str__(self):
        return self.name

class book(models.Model):
    name=models.ForeignKey(author,on_delete=models.CASCADE)
    bookname=models.CharField(max_length=50)


class shubham(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name