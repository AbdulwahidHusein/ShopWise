from rest_framework import permissions

class IsUserItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, item):
        if item.shop:
            return item.shop.seller.id == request.user.id
        return True

class IsUserShopOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.seller.id == request.user.id
