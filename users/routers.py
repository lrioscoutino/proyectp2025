from rest_framework import routers
from users.viewsets import ProductViewset

router = routers.DefaultRouter()

router.register(
    'products',
    ProductViewset
)