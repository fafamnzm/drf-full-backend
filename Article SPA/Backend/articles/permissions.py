from rest_framework import permissions


class IsAthourOrReadOnly(permissions.BasePermission):
    
    # def has_permission(self, request, view):
    #     if view.action == 'create':
    #         return False # request.user and request.user.is_authenticated
    #     return True

    def has_object_permission(self, request, view, obj):
        # allowing read only requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # custome permission
        #print(obj.author)
        return obj.author == request.user
