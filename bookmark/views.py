# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답

from django.views import generic

from django.urls import reverse_lazy
from .models import Bookmark

class ListView(generic.ListView):
    model = Bookmark

class CreateView(generic.CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'

class DetailView(generic.DetailView):
    model = Bookmark
    template_name_suffix = '_detail'

class UpdateView(generic.UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class DeleteView(generic.DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')