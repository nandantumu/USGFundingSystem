from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    # inventorycontrol/
    path('', views.index, name='Organizations'),
    # inventorycontrol/organization/5
    path('organization/<int:org_id>/', views.org_detail, name='Organization Detail'),
    # inventorycontrol/inventory
    path('inventory/', views.inventory, name="Inventory"),
    # inventorycontrol/inventory/2
    path('inventory/<int:inv_id>/', views.inv_detail, name='Inventory Detail')
]
