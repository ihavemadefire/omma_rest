from django.urls import path
from .views import NotAPageView, DispensaryDetail, DispensaryList

urlpatterns = [
    path('dispensary/<int:pk>',DispensaryDetail.as_view(), name='dispensary_view'),
    path('dispensary/', DispensaryList.as_view(), name='dispensary_list'),
]
