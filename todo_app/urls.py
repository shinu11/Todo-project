from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    # path('result',views.result,name='result')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('objtask/',views.TaskListView.as_view(),name='objtask'),
    path('objdetail/<int:pk>/',views.TaskDetailView.as_view(),name='objdetail'),
    path('objupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='objupdate'),
    path('objdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='objdelete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)