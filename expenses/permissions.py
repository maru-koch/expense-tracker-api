from rest_framework.permissions import BasePermission

class Is_owner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user