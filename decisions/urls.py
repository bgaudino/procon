from django.urls import path

from . import views

urlpatterns = [
    path("", views.DecisionView.as_view(), name="index"),
    path("<int:pk>/", views.DecisionDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.DecisionDeleteView.as_view(), name="delete"),
    path("create/", views.NewDecisionView.as_view(), name="create"),
    path("<int:pk>/update/", views.DecisionUpdateView.as_view(), name="update"),
    path("options/create/", views.NewOptionView.as_view(), name="options_create"),
    path(
        "options/<int:pk>/update/",
        views.OptionUpdateView.as_view(),
        name="options_update",
    ),
    path(
        "options/<int:pk>/delete/",
        views.OptionDeleteView.as_view(),
        name="options_delete",
    ),
    path("options/<int:pk>/choose/", views.OptionChooseView.as_view(), name="options_choose"),
    path("pros/create/", views.NewProView.as_view(), name="pros_create"),
    path("cons/create/", views.NewConView.as_view(), name="cons_create"),
    path("pros/<int:pk>/delete/", views.ProDeleteView.as_view(), name="pros_delete"),
    path("cons/<int:pk>/delete/", views.ConDeleteView.as_view(), name="cons_delete"),
    path("pros/<int:pk>/update/", views.ProUpdateView.as_view(), name="pros_update"),
    path("cons/<int:pk>/update/", views.ConUpdateView.as_view(), name="cons_update"),
]
