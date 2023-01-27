from datetime import datetime

from balaboba import Balaboba
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bb = Balaboba()
        intros = bb.intros("ru")
        news = [bb.balaboba("Новость", intro=intro.number) for intro in intros]
        context = {
            "news_cards": [
                {"header": " ".join(new.split()[0:3]) + "...", "news": new, "date": datetime.now()} for new in news
            ]
        }
        print(context)
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context
