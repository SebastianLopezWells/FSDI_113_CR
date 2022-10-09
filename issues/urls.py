from django.urls import path
from .views import (
    IssueListView,
    ToDoIssueListView,
    InProgressIssueListView,
    DoneIssueListView,
    IssueDetailView,
    IssueCreateView,
    IssueUpdateView,
    IssueDeleteView
)


urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    path('todo/', ToDoIssueListView.as_view(), name='todo_list'),
    path('inprogress/', InProgressIssueListView.as_view(), name='inprogress_list'),
    path('done/', DoneIssueListView.as_view(), name='done_list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('create/', IssueCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='delete'),
]
