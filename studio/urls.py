"""
URL configuration for studio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studio_app import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

# <!-----------------------HOME PAGE---------------------------!>



    path('about', views.about),
    path('admin_contact', views.admin_contact),
    path('',views.index),
    path('portfolio',views.portfolio),
    path('contact', views.contact_fu),
    path('register', views.register,name='register'),
    path('login', views.login,name='login'),
    path('logout',views.logout_ua),


# <!-----------------------USER PAGE---------------------------!>


    path('user_index/<int:id>',views.user_index),
    path('user_booking',views.user_booking),
    path('user_frames',views.user_frames),
    path('user_appoinment',views.user_appoinment),
    path('user_design',views.user_design),
    path('user_logout',views.user_logout),
    path('feedback', views.user_feedback),
    path('myproduct/<int:id>', views.myproduct),#<!____USER ORDER____!>

    path('response_booking', views.response_booking),
    path('response_appoinment', views.response_appoinment),
    path('response_design', views.response_design),
    path('response_order', views.response_order),

# <!-----------------------ADMIN PAGE---------------------------!>
    path('displaygallery', views.displaygallery),
    path('admin_gallery', views.admin_gallery),
    path('admin_index',views.admin_index),
    path('admin_feedback', views.admin_feedback),
    path('admin_addframe',views.admin_addframe),
    path('admin_frameedit/<int:id>', views.admin_frameedit),
    path('admin_framedelete/<int:id>', views.admin_framedelete),
    path('admin_view_user',views.admin_view_user),
    path('admin_index',views.admin_index),
    path('admin_booking/<int:id>', views.admin_booking),
    path('admin_booking', views.admin_booking_table),

    path('admin_appoinment/<int:id>', views.admin_appoinment),
    path('admin_appoinment', views.admin_appoinment_table),
    path('admin_design', views.admin_design),
    path('admin_designstatus/<int:id>', views.admin_designstatus),
    path('admin_displayframes', views.admin_displayframes),
    path('admin_order', views.admin_order),
    path('admin_orderstatus/<int:id>', views.admin_orderstatus),

# <!-----------------------ADMIN RESPONSE IN USER SIDE---------------------------!>
    path('status_design', views.status_design),
    path('success_booking/<int:id>', views.success_booking),
    path('success_order/<int:id>', views.success_order),
    path('success_design/<int:id>', views.success_design),


# <!-----------------------FORGOT PASSWORD---------------------------!>

    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_password,name='reset_password'),



# <!-----------------------CART PAGE---------------------------!>


    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:addframe_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('payment/<int:id>/<int:amount>', views.payment),
    path('payment_order/<int:id>/<int:amount>', views.payment_order),
    path('payment_design/<int:id>/<int:amount>', views.payment_design),
    path('payment_message', views.payment_message),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
