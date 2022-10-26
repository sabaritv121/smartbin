from django.urls import path

from binapp import views

urlpatterns = [

    # path('',views.hello,name='welcome'),
    path('',views.index,name='inde'),
    path('login', views.login_view, name='login'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('adminhome', views.adminhome, name='adminhome'),
    path("dash",views.dashboard,name="dashboard"),
    path('register', views.registeruser, name='register'),
    path('driregister', views.registerdriver, name='driregister'),
    path('base', views.base, name='base'),
    path('userhome', views.userhome, name='userhome'),
    path('add_bin', views.add_bin, name='add_bin'),
    path('viewbin', views.garbage, name='viewbin'),
    path('admin_viewnotification', views.admin_viewnotification, name='admin_viewnotification'),

    path('map_view1/<int:id>/', views.map_view1, name='map_view1'),
    path('iotdata', views.iotdata, name='iotdata'),
    path('driotdata', views.driver_iotdata, name='driotdata'),
    path('postnotification', views.postnotification, name='postnotification'),




    path('driverhome', views.driverhome, name='driverhome'),
    path('viewdriver', views.viewdriver, name='viewdriver'),
    path('viewuser', views.viewuser, name='viewuser'),
    path('postcomplaint', views.postcomplaint, name='postcomplaint'),
    path('viewcomplaint', views.viewcomplaint, name='viewcomplaint'),
    path('viewusercomplaint', views.viewcmpuser, name='viewusercomplaint'),
    path('postuserreply/<int:id>/', views.postuserreply, name='postuserreply'),
    path('postdrivercomplaint', views.postdrivercomplaint, name='postdrivercomplaint'),
    path('viewdrivercomplaint', views.viewdrivercomplaint, name='viewdrivercomplaint'),
    path('postdriverreply/<int:id>/', views.postdriverreply, name='postdriverreply'),
    path('viewdrivercmp', views.viewdrivercmp, name='viewdrivercmp'),
    # path('viewuserprof', views.viewuserprof, name='viewuserprof'),

    path('notification',views.notification,name='notification'),
    path('postrequest', views.postrequest, name='postrequest'),
    path('viewrequest', views.viewrequest, name='viewrequest'),
    path('viewrequeststs', views.viewrequeststs, name='viewrequeststs'),
    path('viewnotification', views.viewnotification, name='viewnotification'),

    path('approve_user/<int:id>/', views.approve_user, name='approve_user'),
    # path('reject_user/<int:id>/', views.reject_user, name='reject_user'),
    # path('reject_driver/<int:id>/', views.reject_driver, name='reject_driver'),
    path('approve_driver/<int:id>/', views.approve_driver, name='approve_driver'),
    path('approve_birequest/<int:id>/', views.approve_birequest, name='approve_birequest'),
    path('reject_binrequest/<int:id>/', views.reject_binrequest, name='reject_binrequest'),
    path('subscribe', views.subscribe, name='subscribe'),

#driver
    path('garbage_userview', views.garbage_userview, name='garbage_userview'),
]
