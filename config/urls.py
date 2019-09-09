from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from bank.api import BranchIFSCView, BankBranchView
from bank.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/branch-ifsc/(?P<ifsc_code>.*)/$', BranchIFSCView.as_view(), name="branch-ifsc"),
    url(r'^api/bank-branch/$', BankBranchView.as_view(), name="bank-branch"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
