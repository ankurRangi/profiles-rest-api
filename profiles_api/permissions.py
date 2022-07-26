from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Aloow user to make changes/edit to their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is tring to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
