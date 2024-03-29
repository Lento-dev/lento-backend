from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
  

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
    
class SaveIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_n == request.user
    
    
class ReadOnlyuser(permissions.BasePermission):
  
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else: 
            return False

       
