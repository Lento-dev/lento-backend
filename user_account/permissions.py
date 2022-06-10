from rest_framework import permissions


class Authorauthenticatedorhasaccess(permissions.BasePermission):

    
    def has_object_permission(self, request, view, obj):
       
        return  request.user.is_authenticated and obj.access_profile 
           
        
   
       