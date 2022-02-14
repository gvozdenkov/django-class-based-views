from django.urls import path

from hello import views

urlpatterns = [
    path('', views.MessageView.as_view(success_url='/thank-you'), name='hello_there'),
    path('thank-you', views.ThankyouView.as_view(), name='thankyou'),
    path('messages', views.MessageListView.as_view(), name='all_messages'),
    path('messages/<int:pk>', views.MessageDetailView.as_view(), name='detail_message')
]
