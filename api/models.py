import builtins
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from api.managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.

ROLES = (
    ('0', 'employee'),
    ('1', 'teamlead'),
    ('2', 'boss'),
)

GENDERS = (
    ('1', 'male'),
    ('2', 'female'),
    ('3', 'unknown')
)

LEVELS = (
    ('1', 'junior'),
    ('2', 'middle'),
    ('3', 'senior'),
    ('4', 'teamlead'),
)



class position(models.Model):
    level = models.CharField(choices=LEVELS, blank = True, max_length=10)
    title = models.CharField(max_length=50, blank=True)
    salary = models.FloatField()

    def __str__(self):
        return self.title + ' (' + str(self.salary) + ')'



class CustomUser(AbstractUser):
    role = models.CharField(choices = ROLES, default="0", max_length = 20)
    position = models.ForeignKey(position, on_delete = models.PROTECT, null=True)
    first_name = models.CharField(max_length = 50, null = False)
    last_name = models.CharField(max_length = 100)
    father_Name = models.CharField(max_length = 100)
    email = models.EmailField(_('email adress'),unique=True)
    vacationName = models.CharField(max_length = 200)
    vacationRole = models.CharField(max_length = 150)
    manager = models.CharField(max_length=150)
    passManager = models.CharField(max_length = 150)
    phone = models.IntegerField(null=True)
    extraPhone = models.IntegerField(null=True, blank=True)
    spentaimes = models.TextField(blank=True)
    remote = models.BooleanField(default = False)
    skype = models.CharField(max_length = 36, blank=True, null=True)
    telegram = models.CharField(max_length = 32, blank=True, null=True)
    birthday = models.DateField(null=True)
    office = models.CharField(max_length = 60)
    division = models.CharField(max_length = 100)
    entity = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100)
    employment = models.DateField(null=True)
    workStart = models.DateField(null=True)
    lastChanged = models.DateTimeField(null=True)
    admChanged = models.CharField(default="boss", max_length=50)
    gender = models.CharField(choices = GENDERS, blank = False, default = '3', max_length = 10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email + ' (' + self.first_name + ' ' + self.last_name + ')'


class finance_request(models.Model):
    text = models.CharField(max_length=100, blank=False)
    price = models.FloatField(null=True)
    approved = models.BooleanField(default = False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.text) + " (" + str(self.price) + ")" + " for " + str(self.owner.first_name) + " " + str(self.owner.last_name) 
        
class vacation_request(models.Model):
    first_date = models.DateField(null = True)
    last_date = models.DateField(null = True)
    paid = models.BooleanField(default = True)
    contact = models.IntegerField(blank=False, null=True)
    worker = models.CharField(blank=True, max_length=100)
    approved = models.BooleanField(default = False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.owner.first_name)  + " " + str(self.owner.last_name) + " (" + str(self.first_date) + str(self.owner.last_date) + " " + ")"

class sick_request(models.Model):
    first_date = models.DateField(null = True)
    last_date = models.DateField(null = True)
    case = models.TextField(blank = False)
    contact = models.IntegerField(blank=False, null=True)
    worker = models.CharField(blank=True, max_length=100)
    approved = models.BooleanField(default = False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.owner.first_name)  + " " + str(self.owner.last_name) + " (" + str(self.first_date) + str(self.owner.last_date) + " " + ")"

class long_sick_request(models.Model):
    first_date = models.DateField(null = True)
    last_date = models.DateField(null = True)
    case = models.TextField(default="Заболел")
    contact = models.IntegerField(blank=False, null=True)
    worker = models.CharField(blank=True, max_length=100)
    document = models.FileField()
    approved = models.BooleanField(default = False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.owner.first_name)  + " " + str(self.owner.last_name) + " (" + str(self.first_date) + str(self.owner.last_date) + " " + ")"

class survey(models.Model):
    important = models.BooleanField(default=False)
    title = models.CharField(max_length = 50)
    finished = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title)

class question(models.Model):
    number = models.IntegerField(primary_key=True)
    text = models.TextField()
    survey = models.ForeignKey(survey, on_delete=models.CASCADE)

class answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(question, on_delete=models.CASCADE)

class event(models.Model):
    paid = models.BooleanField(default=True)
    price = models.FloatField(blank = True, null = True)
    theme = models.CharField(blank = False, max_length = 50, default = "iOS Разработка")
    type = models.CharField(blank = False, max_length = 50, default = "Выступление спикера")
    format = models.CharField(blank = False, max_length = 50, default = "Дистанционное мероприятие")
    title = models.CharField(max_length=50)
    datetime = models.DateTimeField(null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

class task(models.Model):
    target = models.BooleanField(default = False)
    todo = models.CharField(blank=False, null=True, max_length=50)
    done = models.BooleanField(default=False)
    proof = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=CASCADE)
    file = models.FileField(null=True, blank=True)