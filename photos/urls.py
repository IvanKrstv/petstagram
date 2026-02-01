from django.urls import path, include

urlpatterns = (
    path('add/', ),
    path('<int:pk>/', include([
        path('', ),
        path('edit/', )
    ]))
)