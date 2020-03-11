from rest_framework.serializers import ModelSerializer
from todoapp.models import Task

class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user',)

class TaskListSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'create', 'user', 'status_type', 'id']

class TaskDetailSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDeleteSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user',)
