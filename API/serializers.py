from rest_framework import serializers
from Projects.models import Project


class ProjectDetailsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Project
        fields = ["user","project_external_image","project_name","project_description","project_url","project_github_repo"]