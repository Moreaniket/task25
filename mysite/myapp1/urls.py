from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('myapp1.urls'))
    path('',views.home),
    path('save',views.save),
    path('signin',views.signin),
    path('check',views.check),
    path('reset',views.reset),
    path('resetps',views.resetps),
    path('shubham/<int:id>',views.one),
    path('list',views.list),
    path('add',views.add),
    path('update',views.update),
    path('delete',views.delete),
    path('login',views.login),
    path('calculate',views.calculate),

]
