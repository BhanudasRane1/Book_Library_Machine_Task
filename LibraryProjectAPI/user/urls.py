from django.contrib import admin
from django.urls import path


from user.views import BookAPIView,BookDetails,BookPost
urlpatterns = [

path('books/',BookAPIView.as_view()),
path('book_post/',BookPost.as_view()),
     
path('books_detail/<int:id>/',BookDetails.as_view()),




    
    
]
