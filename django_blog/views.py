from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
