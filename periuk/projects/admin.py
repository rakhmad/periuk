from django.contrib import admin

from projects.models import Projects, Tasks

class TasksAdmin(admin.ModelAdmin):
  pass

class ProjectsAdmin(admin.ModelAdmin):
  pass

admin.site.register(Tasks, TasksAdmin)
admin.site.register(Projects, ProjectsAdmin)

