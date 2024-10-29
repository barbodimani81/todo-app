from rest_framework import serializers

from ...models import Task
from accounts.models import Profile


class TaskSerializer(serializers.ModelSerializer):
    rel_url = serializers.URLField(source='get_relative_url', read_only=True)
    abs_url = serializers.SerializerMethodField(method_name='get_abs_url')
    readonly_fields = ['author']

    class Meta:
        model = Task
        fields = ['id', 'author', 'title', 'description', 'done', 'rel_url', 'abs_url']

    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('rel_url', None)
            rep.pop('abs_url', None)
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)

