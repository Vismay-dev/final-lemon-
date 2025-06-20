from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu-viewset', views.MenuItemViewset, basename='menuitems')

urlpatterns = [
    path('', include(router.urls)),
    path('menu/', views.menuItemListCreateView.as_view(), name="MenuItem-ListCreateAPIView"),
    path('menu/<int:id>', views.menuItemRetrieveView.as_view(), name="MenuItem-RetrieveAPIView"),
    path('menu/<int:id>/update', views.menuItemUpdateView.as_view(), name="MenuItem-UpdateAPIView"),
    path('menu/<int:id>/destroy', views.menuItemDestroyView.as_view(), name="MenuItem-DestroyAPIView"),
]

# urlpatterns = [
#     path('menu-items/', views.menuItems, name='MenuItems-FBVs'),
#     path('menu-items/<int:id>', views.singleMenuItem, name='menuItem-FBVs-ById'),
#     path('menu-items/<int:id>', views.singleMenuItem, name='menuItem-FBVs-ById'),
#     path('menu-items/create', views.createMenuItem, name='createMenuItem-FBVs-ById'),
#     path('menu-items/paginated', views.getMenuItem, name='getMenuItem-FBVs-ById'),
# ]