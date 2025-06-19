from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'description', 'status', 'due_date', 'created_at', 'is_overdue']
        read_only_fields = ['project', 'created_at', 'is_overdue']
    
    def validate_project(self, value):
        if value.created_by != self.context['request'].user:
            raise serializers.ValidationError("You don't have permission to add tasks to this project.")
        return value