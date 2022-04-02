from django.urls import include, path
from .views import CustomerCreate, CustomerList, CustomerDetail, CustomerUpdate, CustomerDelete, OrderCreate, OrderList, OrderDetail, OrderUpdate, OrderDelete

urlpatterns = [
    path('create/', CustomerCreate.as_view(), name='create-customer'), # POST
    path('', CustomerList.as_view()), # GET
    path('<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'), # GET
    path('update/<int:pk>', CustomerUpdate.as_view(), name='update-customer'), # PUT
    path('delete/<int:pk>', CustomerDelete.as_view(), name='delete-customer'), # DELETE

    # ORDER
    path('order/create/', OrderCreate.as_view(), name='create-order'), # POST
    path('order/', OrderList.as_view()), # GET
    path('order/<int:pk>/', OrderDetail.as_view(), name='retrieve-order'), # GET
    path('order/update/<int:pk>', OrderUpdate.as_view(), name='update-order'), # PUT
    path('order/delete/<int:pk>', OrderDelete.as_view(), name='delete-order') # DELETE
]