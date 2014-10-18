# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    HoldingPublishView,
    HoldingUpdateView,
    TitlePublishView,
    TitleUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^holding/(?P<pk>\d+)/publish/$',
        view=HoldingPublishView.as_view(),
        name='compose.holding.publish'
        ),
    url(regex=r'^holding/(?P<pk>\d+)/edit/$',
        view=HoldingUpdateView.as_view(),
        name='compose.holding.update'
        ),
    url(regex=r'^title/(?P<pk>\d+)/publish/$',
        view=TitlePublishView.as_view(),
        name='compose.title.publish'
        ),
    url(regex=r'^title/(?P<pk>\d+)/edit/$',
        view=TitleUpdateView.as_view(),
        name='compose.title.update'
        ),
)