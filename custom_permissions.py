from rest_framework import permissions

class IsUserItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
    
