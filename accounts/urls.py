from django.urls import path, include

urlpatterns = (
    path('register/', ),
    path('login/', ),
    path('profile/<int:pk>/', include([
        path('edit/', ),
        path('delete/', )
    ]))
)