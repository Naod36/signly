"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static
# from core.views import serve_pdf  # Adjust this import to match where serve_pdf is actually located


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('', include('core.urls')),
    path('upload/', views.upload, name='upload'),  # ✅ This is the missing piece
    path('pdf/<int:pk>/', views.view_pdf, name='view_pdf'),
    path("draw-signature/", views.draw_signature, name="draw_signature"),
    # path('serve-pdf/<str:filename>/', serve_pdf, name='serve_pdf'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
