from django.db import models

from django.contrib.auth.models import User

"""
  Use Django Built-in User class and adding some
  features.
"""

class MyUser(User):
  
  class Meta:
    proxy = True

  def __unicode__(self):
    return self.full_name()

  def full_name(self):
    return self.first_name + " " + self.last_name

# Create your models here.
class Projects(models.Model):

  ## Fields
  name = models.CharField(max_length = 200, verbose_name = u'Nama')
  desc = models.TextField(verbose_name = u'Deskripsi')
  start = models.DateField(verbose_name = u'Mulai')
  end = models.DateField(verbose_name = u'Selesai')

  leader = models.ForeignKey('MyUser', verbose_name = u'Ketua', 
      limit_choices_to = { 'is_staff' : False })
  members = models.ManyToManyField('MyUser', related_name = '+', 
      verbose_name = u'Anggota', limit_choices_to = { 'is_staff' : False })

  def __unicode__(self):
    return "[" + self.name + "]"

  def get_members(self):
    return self.members.all()

class Tasks(models.Model):
  def __unicode__(self):
    return "[" + self.project.name + "] -> " + self.name 

  PRIORITIES = (
      (u'Normal', 1),
      (u'Immediate', 2),
      (u'Urgent', 3),
      (u'Critical', 4),
  )

  TYPES = (
      (u'Feature', 1),
      (u'Bug', 2),
  )

  STATUS = (
      (u'Closed', 1),
      (u'Open', 2),
      (u'Resolved', 3),
      (u'Wont Fix', 4),
      (u'Re-open', 5),
      (u'Duplicate', 6),
  )

  name = models.CharField(max_length = 200, verbose_name = u'Judul')
  desc = models.TextField(verbose_name = u'Penjelasan Singkat')
  reporter = models.ForeignKey('MyUser', related_name = '+', 
      limit_choices_to = { 'is_staff' : False })
  assignee = models.ForeignKey('MyUser', related_name = '+',
      limit_choices_to = { 'is_staff' : False })
  types  = models.CharField(max_length= 15, choices = TYPES, verbose_name = u'Tipe')
  priority = models.CharField(max_length= 15, choices = PRIORITIES, verbose_name = u'Prioritas')
  status = models.CharField(max_length= 15, choices=STATUS, verbose_name = u'Status')
  belongs_to = models.ForeignKey(Projects)


