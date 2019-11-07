from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.home, name="homes")
    path("coffee/<id>/buy", app.views.buy_coffee, name="buy_coffee"),
    path("transaction/<id>", app.views.transaction, name="transaction_detail")
    ]

