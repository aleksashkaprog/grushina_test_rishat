from django.urls import path

from .views import ItemDetailView, SuccessView, CancelView, \
    CreateCheckoutSessionView


urlpatterns = [
    path('buy/<int:pk>', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item-detail'),
    path('success', SuccessView.as_view(), name='success'),
    path('cancel', CancelView.as_view(), name='cancel'),
]