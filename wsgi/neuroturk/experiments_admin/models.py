from django.db import models

# Create your models here.


class Experiment(models.Model):
    assignment = None
    pass


class Assignment(models.Model):
    pass


class SingleResult(models.Model):
    assignment = None
    recruitment_environment = None
    subject = None
    pass


class Subject(models.Model):
    pass


class RecruitmentEnvironment(models.Model):
    pass


class AmazonTurkRE(RecruitmentEnvironment):
    pass


class MailingListRE(RecruitmentEnvironment):
    pass
