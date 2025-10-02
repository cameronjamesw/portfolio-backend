from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # If safe method (GET, HEAD, OPTIONS), allow anyone
        if request.method in SAFE_METHODS:
            return True

        # If not authenticated → 401
        if not request.user or not request.user.is_authenticated:
            return False

        # Only admin users can write
        return request.user.is_staff
