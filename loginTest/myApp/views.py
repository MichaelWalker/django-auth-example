from django.http import HttpResponse
from rest_framework import viewsets
from loginTest.myApp.models import Item
from loginTest.myApp.serializers import ItemSerializer
from django.views.generic import ListView
from django.contrib.auth.mixins import AccessMixin
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import BasePermission


class StaffLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IsAuthenticatedMember(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and not request.user.is_staff


def index(request):
    return HttpResponse("Hello World!")


class ItemListView(StaffLoginRequiredMixin, ListView):
    model = Item
    template_name = "myApp/item_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['items'] = Item.objects.all()
        return context


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedMember]
