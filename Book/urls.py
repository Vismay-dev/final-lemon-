from django.urls import path
from . import views

urlpatterns = [
    path("", views.Greet, name="Greet-View"),
    path('create-book/', views.create_book, name="POST-Book"),
    path('<int:id>/', views.get_book, name="GET-Book-ById"),
    path('all-books/', views.get_allBooks, name="GET-AllBooks"),
    path('<int:id>/put-book/', views.put_book, name="PUT-PATCH-Book-ById"),
    path('<int:id>/delete-book/', views.delete_book, name="DELETE-Book-ById"),
    # Below are the APIs of DRF
    path('book/', views.book, name='Book-DRF'),
    # API for the class named BookView using ViewSet
    path('book-view/', views.BookView.as_view(
            {
                'get' : 'list',
                'post' : 'create',
            }
        ), name='Book-view'),
    path('book-view/<int:id>/', views.BookView.as_view(
            {
                'get' : 'retrieve',
                'put' : 'update',
                'patch' : 'update',
                'delete' : 'delete',
            }
        ), name="Book-view-ById"),
    
]





# # _____________________________________________________________________

#                     # Routing Via Simple Router
# # _____________________________________________________________________
# from rest_framework.routers import SimpleRouter
# from . import views
# router = SimpleRouter(trailing_slash=False)

# # router.register('books', views.BookView, basename='books')


# urlpatterns = router.urls



# __________________________________________________________________________

                # Setting APIs for CBVs that extends generic views
# __________________________________________________________________________


from . import views
from django.urls import path

urlpatterns = [
    path('book/', views.BookListCreateView.as_view(), name='BookListCreateView'),
    path('book/<int:id>/', views.BookRetrieveView.as_view(), name='BookRetrieveView'),
    path('book/<int:id>/update/', views.BookUpdateView.as_view(), name='BookUpdateView'),
    path('book/<int:id>/delete/', views.BookDeleteView.as_view(), name="BookDetroyView"),
    
]
