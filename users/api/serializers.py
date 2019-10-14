from rest_framework import serializers
from users.models import User, StudyGroup


class SerializerUser(serializers.ModelSerializer):
    fullname = serializers.ReadOnlyField()
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
        return obj.studygroup_id


class SerializerStudyGroup(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = (
            'id',
            'name'
        )
