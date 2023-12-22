"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#后台管理子路由文件
from django.contrib import admin
from django.urls import path
from MyAdmin.views import index
from MyAdmin.views import Employee
from MyAdmin.views import Member
from MyAdmin.views import Drug
from MyAdmin.views import category

urlpatterns = [
    # homepage of background.
    path('', index.index, name = 'MyAdmin_index'),

    # 后台管理员路由
    path('login', index.login, name = "MyAdmin_login"),   # loading login form.
    path('dologin', index.dologin, name = "MyAdmin_dologin"), # promoting login.
    path('logout', index.logout, name = "MyAdmin_logout"),    # logout.
    #path('verify', index.verify, name="MyAdmin_verify"), #验证码


    # employee management.
    path('Employee/<int:pIndex>', Employee.index, name = 'MyAdmin_emp_index'),
    path('Employee/add', Employee.add, name = 'MyAdmin_emp_add'),
    path('Employee/insert', Employee.insert, name = 'MyAdmin_emp_insert'),
    path('Employee/del/<int:eid>', Employee.delete, name = 'MyAdmin_emp_delete'),
    path('Employee/edit/<int:eid>', Employee.edit, name = 'MyAdmin_emp_edit'),
    path('Employee/update/<int:eid>', Employee.update, name = 'MyAdmin_emp_update'),
    # reset employee's password.
    #path('user/resetpass/<int:uid>', user.resetpass, name="myadmin_user_resetpass"),
    #path('user/doresetpass/<int:uid>', user.doresetpass, name="myadmin_user_doresetpass"),

    #用户管理路由
    path('Member/<int:pIndex>', Member.index, name="MyAdmin_mem_index"), #浏览用户

    # 菜品信息管理
    path('Drug/<int:pIndex>', Drug.index, name="MyAdmin_product_index"),
    path('Drug/add', Drug.add, name="MyAdmin_product_add"),
    path('Drug/insert', Drug.insert, name="MyAdmin_product_insert"),
    path('Drug/del/<int:id>', Drug.delete, name="MyAdmin_product_del"),
    path('Drug/edit/<int:id>', Drug.edit, name="MyAdmin_product_edit"),
    path('Drug/update/<int:id>', Drug.update, name="MyAdmin_product_update"),

    #药品种类
    path('Category/<int:pIndex>', category.index, name="MyAdmin_Category_index"),
    path('Category/add', category.add, name="MyAdmin_Category_add"),
    path('Category/insert', category.insert, name="MyAdmin_Category_insert"),
    path('Category/del/<int:id>', category.delete, name="MyAdmin_Category_del"),
    path('Category/edit/<int:id>', category.edit, name="MyAdmin_Category_edit"),
    path('Category/update/<int:id>', category.update, name="MyAdmin_Category_update"),



]
