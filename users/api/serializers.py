from rest_framework import serializers
from users.models import StudyGroup
from django.contrib.auth.models import User


class SerializerUser(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField('get_full_name', read_only=True)
    rank = serializers.SerializerMethodField('get_rank', read_only=True)
    group = serializers.SerializerMethodField('get_study_group_id', read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'fullname',
            'rank',
            'group',
        )

    def get_study_group_id(self, obj):
        return obj.studyprofile.studygroup_id

    def get_rank(self, obj):
        return obj.studyprofile.rank

    def get_full_name(self, obj):
        return f'{obj.last_name} {obj.first_name}'


class SerializerStudyGroup(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = (
            'id',
            'name'
        )
