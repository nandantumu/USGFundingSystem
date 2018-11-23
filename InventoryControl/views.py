from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Organization, InventoryItem, Sanction
from django.views import generic

# Create your views here.


def index(request):
    org_list = Organization.objects.all()
    return render(request, 'InventoryControl/all_orgs.html', {'org_list': org_list})


def org_detail(request, org_id):
    org = get_object_or_404(Organization, pk=org_id)
    sanction_list = Sanction.objects.all().filter(organization__exact=org_id)
    inv_list = InventoryItem.objects.all().filter(organization__exact=org_id)
    return render(request, 'InventoryControl/org_detail.html', {'org': org,
                                                                'sanction_list': sanction_list,
                                                                'inventory_list': inv_list})


def inventory(request):
    inventory_list = InventoryItem.objects.all()
    return render(request, 'InventoryControl/all_inventory.html', {'inv_list': inventory_list})


def inv_detail(request, inv_id):
    inv_item = get_object_or_404(InventoryItem, pk=inv_id)
    return render(request, 'InventoryControl/inventory_detail.html', {'item': inv_item})
