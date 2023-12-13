from django.urls import path
from . import views

app_name = "bookmark"
urlpatterns = [
    # http://127.0.0.1/bookmark/
    path("",                 views.ListView.as_view(),   name='list'),
    path("add/",             views.CreateView.as_view(), name='add'),
    path("detail/<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("update/<int:pk>/", views.UpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", views.DeleteView.as_view(), name='delete'),
]