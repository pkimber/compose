# -*- encoding: utf-8 -*-
import factory

from block.tests.factories import PageSectionFactory
from compose.models import (
    Article,
    ArticleBlock,
    Calendar,
    CalendarBlock,
    CodeSnippet,
    Map,
    MapBlock,
    Sidebar,
    SidebarBlock,
    Slideshow,
    SlideshowBlock,
    SlideshowImage,
    Feature,
    FeatureBlock,
    Header,
    HeaderBlock,
)


class ArticleBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = ArticleBlock


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Article

    block = factory.SubFactory(ArticleBlockFactory)

    @factory.sequence
    def order(n):
        return n


class CalendarBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = CalendarBlock


class CalendarFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Calendar

    block = factory.SubFactory(CalendarBlockFactory)

    @factory.sequence
    def order(n):
        return n


class CodeSnippetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CodeSnippet

    @factory.sequence
    def slug(n):
        return 'slug_{:02d}'.format(n)


class FeatureBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = FeatureBlock


class FeatureFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Feature

    block = factory.SubFactory(FeatureBlockFactory)

    @factory.sequence
    def order(n):
        return n


class HeaderBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = HeaderBlock


class HeaderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Header

    block = factory.SubFactory(HeaderBlockFactory)

    @factory.sequence
    def order(n):
        return n


class MapBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = MapBlock


class MapFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Map

    block = factory.SubFactory(MapBlockFactory)

    @factory.sequence
    def order(n):
        return n


class SidebarBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = SidebarBlock


class SidebarFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Sidebar

    block = factory.SubFactory(SidebarBlockFactory)

    @factory.sequence
    def order(n):
        return n


class SlideshowBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = SlideshowBlock


class SlideshowImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SlideshowImage


class SlideshowFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Slideshow

    block = factory.SubFactory(SlideshowBlockFactory)

    @factory.sequence
    def order(n):
        return n
