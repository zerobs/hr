from django.conf.urls import patterns,url


urlpatterns = patterns('leave.views',
                       url(r'^$','home'), # welcome page
                       url(r'^employee/(\d+)/?$','detail_employee'),# detailed employee page
                       url(r'^all/?$','all')#show all employees saved in database
                       )
