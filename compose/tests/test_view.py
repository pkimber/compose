# -*- encoding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import (
    TEST_PASSWORD,
    UserFactory,
)

from block.tests.factories import (
    PageFactory,
    PageSectionFactory,
)
from compose.tests.factories import (
    ArticleFactory,
    CodeSnippetFactory,
    FeatureFactory,
    HeaderFactory,
    SidebarFactory,
    SlideshowFactory,
)


class TestView(TestCase):

    def setUp(self):
        self.user = UserFactory(username='staff', is_staff=True)
        self.assertTrue(
            self.client.login(
                username=self.user.username,
                password=TEST_PASSWORD
            )
        )

    def test_article_create(self):
        p = PageSectionFactory(page=PageFactory(slug_menu=''))
        url = reverse(
            'compose.article.create',
            kwargs=dict(
                page=p.page.slug,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'heading_level': 'h2',
                'title': 'pkimber.net',
                'css_width': settings.CSS_WIDTH_HALFBIG,
                'article_type': settings.CSS_TEXT_LEFT,
                'image_size': settings.CSS_IMAGE_SIZE_HALF,
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_article_create_page_and_menu(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.article.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'heading_level': 'h3',
                'title': 'pkimber.net',
                'css_width': settings.CSS_WIDTH_FULL,
                'article_type': settings.CSS_TEXT_RIGHT,
                'image_size': settings.CSS_IMAGE_SIZE_QUARTER,
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_article_publish(self):
        c = ArticleFactory()
        response = self.client.post(
            reverse('compose.article.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_article_update(self):
        c = ArticleFactory()
        response = self.client.post(
            reverse('compose.article.update', kwargs={'pk': c.pk}),
            {
                'heading_level': 'h2',
                'title': 'pkimber.net',
                'css_width': settings.CSS_WIDTH_HALFBIG,
                'article_type': settings.CSS_TEXT_LEFT,
                'image_size': settings.CSS_IMAGE_SIZE_HALF,
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_article_remove(self):
        c = ArticleFactory()
        response = self.client.post(
            reverse('compose.article.remove', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_code_snippet_list(self):
        url = reverse('compose.code.snippet.list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_code_snippet_create(self):
        url = reverse('compose.code.snippet.create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_code_snippet_update(self):
        snippet = CodeSnippetFactory()
        url = reverse('compose.code.snippet.update', args=[snippet.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_feature_create(self):
        p = PageSectionFactory(page=PageFactory(slug_menu=''))
        url = reverse(
            'compose.feature.create',
            kwargs=dict(
                page=p.page.slug,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'heading_level': 'h2',
                'title': 'pkimber.net',
                'css_width': settings.CSS_WIDTH_HALFBIG,
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_feature_create_page_and_menu(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.feature.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'heading_level': 'h3',
                'title': 'pkimber.net',
                'css_width': settings.CSS_WIDTH_FULL,
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_feature_publish(self):
        c = FeatureFactory()
        response = self.client.post(
            reverse('compose.feature.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_feature_update(self):
        c = FeatureFactory()
        response = self.client.post(
            reverse('compose.feature.update', kwargs={'pk': c.pk}),
            {
                'heading_level': 'h2',
                'title': 'pkimber.net',
                'css_width': settings.CSS_WIDTH_HALFBIG,
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_feature_remove(self):
        c = FeatureFactory()
        response = self.client.post(
            reverse('compose.feature.remove', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_header_create(self):
        p = PageSectionFactory(page=PageFactory(slug_menu=''))
        url = reverse(
            'compose.header.create',
            kwargs=dict(
                page=p.page.slug,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'pkimber1.net',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_header_create_page_and_menu(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.header.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'pkimber2.net',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_header_publish(self):
        c = HeaderFactory()
        response = self.client.post(
            reverse('compose.header.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_header_update(self):
        c = HeaderFactory()
        response = self.client.post(
            reverse('compose.header.update', kwargs={'pk': c.pk}),
            {
                'title': 'pkimber3.net',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_header_remove(self):
        c = HeaderFactory()
        response = self.client.post(
            reverse('compose.header.remove', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_sidebar_create(self):
        p = PageSectionFactory(page=PageFactory(slug_menu=''))
        url = reverse(
            'compose.sidebar.create',
            kwargs=dict(
                page=p.page.slug,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'TITLE',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_sidebar_create_page_and_menu(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.sidebar.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'TITLE',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_sidebar_publish(self):
        c = SidebarFactory()
        response = self.client.post(
            reverse('compose.sidebar.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_sidebar_update(self):
        c = SidebarFactory()
        response = self.client.post(
            reverse('compose.sidebar.update', kwargs={'pk': c.pk}),
            {
                'title': 'TITLE',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_sidebar_remove(self):
        c = SidebarFactory()
        response = self.client.post(
            reverse('compose.sidebar.remove', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_slideshow_create(self):
        p = PageSectionFactory(page=PageFactory(slug_menu=''))
        url = reverse(
            'compose.slideshow.create',
            kwargs=dict(
                page=p.page.slug,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'pkimber.net',
                'slideshow_type': 'text_only',
                'image_size': '1-3',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_slideshow_create_page_and_menu(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.slideshow.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'pkimber.net',
                'slideshow_type': 'text_only',
                'image_size': '1-4',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_slideshow_publish(self):
        c = SlideshowFactory()
        response = self.client.post(
            reverse('compose.slideshow.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_slideshow_update(self):
        c = SlideshowFactory()
        response = self.client.post(
            reverse('compose.slideshow.update', kwargs={'pk': c.pk}),
            {
                'title': 'pkimber.net',
                'slideshow_type': 'text_only',
                'image_size': '1-2',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_slideshow_remove(self):
        c = SlideshowFactory()
        response = self.client.post(
            reverse('compose.slideshow.remove', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)
