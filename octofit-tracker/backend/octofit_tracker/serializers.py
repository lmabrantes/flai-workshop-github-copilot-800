from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    team_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'team', 'team_id']

    def get_id(self, obj):
        return str(obj.pk)

    def get_team(self, obj):
        for team in Team.objects.all():
            if obj.username in (team.members or []):
                return {'id': team.pk, 'name': team.name}
        return None

    def update(self, instance, validated_data):
        team_id = validated_data.pop('team_id', -1)
        old_username = instance.username
        instance = super().update(instance, validated_data)
        new_username = instance.username

        if team_id != -1:
            # Remove user from all teams (use new username; also clean up old username if it changed)
            for team in Team.objects.all():
                changed = False
                members = list(team.members or [])
                if old_username in members:
                    members.remove(old_username)
                    changed = True
                if new_username != old_username and new_username in members:
                    members.remove(new_username)
                    changed = True
                if changed:
                    team.members = members
                    team.save()
            # Add to the selected team
            if team_id:
                try:
                    new_team = Team.objects.get(pk=team_id)
                    members = list(new_team.members or [])
                    if new_username not in members:
                        members.append(new_username)
                        new_team.members = members
                        new_team.save()
                except Team.DoesNotExist:
                    pass
        elif old_username != new_username:
            # Username changed but no team_id provided — update username in existing team
            for team in Team.objects.all():
                members = list(team.members or [])
                if old_username in members:
                    members.remove(old_username)
                    if new_username not in members:
                        members.append(new_username)
                    team.members = members
                    team.save()
                    break

        return instance


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

    def get_id(self, obj):
        return str(obj.pk)


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'date']

    def get_id(self, obj):
        return str(obj.pk)


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score']

    def get_id(self, obj):
        return str(obj.pk)


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'exercises']

    def get_id(self, obj):
        return str(obj.pk)
