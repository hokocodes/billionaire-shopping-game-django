from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Here we are assigning the path of our url
    path('signIn/', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
]