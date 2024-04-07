from rest_framework.permissions import BasePermission, SAFE_METHODS
from users import choices as user_choices

"""
Permission который проверяет у тебя есть роль 'Admin'. Eсли SAFE_METHODS, то все может
"""


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (request.method in SAFE_METHODS) or
            (
                request.user
                and request.user.is_authenticated
                and request.user.user_role == user_choices.UserRole.Admin
            )
        )
