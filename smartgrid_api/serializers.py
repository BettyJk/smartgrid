from rest_framework import serializers
from .models import User, Audit, NonConformite, GridRow
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'role', 'shift')

class NonConformiteSerializer(serializers.ModelSerializer):
    category = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    label = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    chapitre_mlp = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    audit = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = NonConformite
        fields = '__all__'

class AuditSerializer(serializers.ModelSerializer):
    nonconformites = NonConformiteSerializer(many=True)
    user = UserSerializer(read_only=True)
    operator_signature = serializers.CharField(required=False, allow_null=True, allow_blank=True)  # Changed from ImageField
    supervisor_signature = serializers.CharField(required=False, allow_null=True, allow_blank=True)  # Changed from ImageField
    code_route = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    cofor_audite = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    el_bl = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Audit
        fields = ('id', 'date', 'user', 'usine', 'reference', 'global_remark', 'operator_signature', 'supervisor_signature', 'code_route', 'cofor_audite', 'el_bl', 'nonconformites')

    def create(self, validated_data):
        nonconformites_data = validated_data.pop('nonconformites')
        audit = Audit.objects.create(**validated_data)
        for nc_data in nonconformites_data:
            NonConformite.objects.create(audit=audit, **nc_data)
        return audit

class GridRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = GridRow
        fields = '__all__'
