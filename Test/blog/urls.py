from django.urls import path
from . import views # 'views' import ediyoruz.

#   http://127.0.0.1:8000/         ---> index
#   http://127.0.0.1:8000/index    ---> index
#   http://127.0.0.1:8000/blogs    ---> blog
#   http://127.0.0.1:8000/blogs/3  ---> blog-details

urlpatterns = [ #! urlpatterns tanımlıyoruz.
    path("", views.index), # http://127.0.0.1:8000/  
    path("index", views.index), # http://127.0.0.1:8000/index    
    path("blogs", views.blogs), # http://127.0.0.1:8000/blogs    
]  