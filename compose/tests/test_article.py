# -*- encoding: utf-8 -*-
import pytest

from block.tests.helper import check_content
from compose.tests.factories import ArticleFactory


@pytest.mark.django_db
def test_content_methods():
    c = ArticleFactory()
    check_content(c)
