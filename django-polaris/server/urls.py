"""app URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog', include('blog.urls'))
"""
from django.urls import path, include

import polaris.urls
from .views import all_fields_form_view, confirm_email, skip_confirm_email, log_callback,KYC_FORM_VIEW

urlpatterns = [
    path("all-fields", all_fields_form_view),
    path("KYC_FORM", KYC_FORM_VIEW),
    path("confirm_email", confirm_email, name="confirm_email"),
    path("skip_confirm_email", skip_confirm_email, name="skip_confirm_email"),
    path("onChangeCallback", log_callback),
    path("", include(polaris.urls)),
]
