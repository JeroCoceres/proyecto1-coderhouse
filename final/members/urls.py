from django.urls import path
from members.views import membersCreateView, membersListView, update_member, membersDeleteView

urlpatterns = [
    path('members/', membersListView.as_view() ),
    path("new_member/",membersCreateView, name = "new_member"),
    path("update-member/<int:pk>/",update_member),
    path("delete-member/<int:pk>/",membersDeleteView.as_view()),
]