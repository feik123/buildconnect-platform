from rest_framework.exceptions import PermissionDenied


class DisableFormFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            field.disabled = True


class OwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user != request.user:
            raise PermissionDenied('Not allowed')

        return super().dispatch(request, *args, **kwargs)