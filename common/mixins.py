from rest_framework.exceptions import PermissionDenied


class DisableFormFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            field.disabled = True


class OwnerRequiredMixin:
    owner_field = 'user'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        owner = getattr(obj, self.owner_field)
        if owner != request.user:
            raise PermissionDenied('Not allowed')

        return super().dispatch(request, *args, **kwargs)