from django.contrib import messages
from django.contrib.auth import views as auth_views


class LogoutWithMessage(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Ви успішно вийшли зі свого облікового запису!')
        return response
