from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"


class GoodsPageView(TemplateView):
    template_name = "goods.html"