from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from django.shortcuts import get_object_or_404

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Project and all its tasks were deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(
            project_id=project_id,
            project__created_by=self.request.user
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        project = get_object_or_404(
            Project,
            id=self.kwargs['project_id'],
            created_by=self.request.user
        )
        serializer.save(project=project)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(
            project_id=project_id,
            project__created_by=self.request.user
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def patch(self, request, *args, **kwargs):
        if 'status' in request.data and len(request.data) == 1:
            instance = self.get_object()
            instance.status = request.data['status']
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return super().patch(request, *args, **kwargs)