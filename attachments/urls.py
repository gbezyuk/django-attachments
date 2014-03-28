from django.conf.urls import url, patterns

urlpatterns = patterns(
    'attachments.views',
    url(r'^add-for/(?P<app_label>[\w\-]+)/(?P<module_name>[\w\-]+)/(?P<pk>\d+)/$', 'add_attachment', name="add_attachment"),
    url(r'^delete/(?P<attachment_pk>\d+)/$', 'delete_attachment', name="delete_attachment"),
)
