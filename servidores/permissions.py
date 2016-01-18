from rest_framework import permissions

# Classe para verificar se usuário é admin e permitir CRUD em servidores
class IsAdminOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		return request.user.is_superuser == True