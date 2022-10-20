from django.urls import path
from .views import *
urlpatterns=[
path('',NoteListView.as_view(),name='notes-home'),
path('note/<int:pk>/',NoteDetailView.as_view(),name='note-detail'),
path('addnoteyo/',add_note,name='addnote'),
path('note/<int:pk>/updatenote/',UpdateNote,name='note-update'),
path('note/<int:pk>/delete/',NoteDeleteView.as_view(),name='note-delete')
#path('note/new/',NoteCreateView.as_view(),name='note-create')
]
