from rest_framework import permissions

class IsUserItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, item):
        if item.shop:
            return False and item.shop.seller == request.user
        return False
    
