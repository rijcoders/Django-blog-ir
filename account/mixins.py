from django.http import Http404


class FieldMixin():
    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_superuser:
            self.fields = [
            'title','author','slug',
            'category','description','thumbnail',
            'publish','is_special','status'
        ]
        elif self.request.user.is_author:
            self.fields = [
            'title','slug',
            'category','description','thumbnail',
            'publish','is_special'
        ]
        else:
            raise Http404("You cant access this page.")

        return super().dispatch(request, *args, **kwargs)
