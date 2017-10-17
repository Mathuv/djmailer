from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from .views import hello_world

# for DRF class view
from .views import HelloWorldView

# DRF function view
from .views import hello_world_function

# After serializer
from .views import SubscriberView

from .views import SubscriberViewSet, login


router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)


# urlpatterns = [
#     url(r'^login', login),
# ]
#
# urlpatterns += router.urls

urlpatterns = router.urls + [
    url(r'^login', login),
    url(r'^jwt-auth/', obtain_jwt_token),
]



# urlpatterns = [
#     url(r'^hello_plain', hello_world, name="hello_world_plain"),
#     url(r'^hello', HelloWorldView.as_view(), name="hello_world"),
#     url(r'^hello_function', hello_world_function, name="hello_world_function"),
#     url(r'^subscriber', SubscriberView.as_view(), name="subscriber"),
# ]