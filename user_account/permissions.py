from rest_framework import permissions


class Authorauthenticatedorhasaccess(permissions.BasePermission):

    
    def has_object_permission(self, request, view, obj):
       
        if  request.user.is_authenticated:
            return True

        if not(request.user_authenticated) and obj.author.access_profile: 
           return True
        
        return False
        
   
       