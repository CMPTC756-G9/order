import requests
from rest_framework.viewsets import ReadOnlyModelViewSet

from orders.models import Order, Cart
from orders.serializers import OrderSerializer, CartSerializer


class OrderViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user_id = requests.get('xxx'.format(username)).json()['id']
        return Order.objects.filter(user_id=user_id)


class CartViewSet(ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
