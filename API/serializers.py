from rest_framework import serializers
from Projects.models import ProjectDetail


class ProjectDetailsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProjectDetail
        fields = ["user","project_external_image","project_name","project_description","project_url","project_github_repo"]