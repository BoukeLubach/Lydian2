from django.urls import path


from .views import (
    home,
    LoginView, 
    LogoutView, 
    profile, 
    account_view,
    AccountUpdateView,
    MyPasswordChangeView, 
    MyPasswordResetDoneView,
)

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/', profile, name='profile'),
    path('profile/account/', account_view, name='account-view'),
    path('profile/<int:pk>/update-account/', AccountUpdateView.as_view(), name='account-edit'),
    path('profile/change-password/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('profile/change-password/done/', MyPasswordResetDoneView.as_view(), name='password-change-done'),
]

