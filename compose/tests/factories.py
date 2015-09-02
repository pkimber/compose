# -*- encoding: utf-8 -*-
import factory

from block.tests.factories import PageSectionFactory
from compose.models import (
    Article,
    ArticleBlock,
    CodeSnippet,
    Slideshow,
    SlideshowBlock,
    #Feature,
    #FeatureBlock,
    #Header,
    #HeaderBlock,
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


class CodeSnippetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CodeSnippet

    @factory.sequence
    def slug(n):
        return 'slug_{:02d}'.format(n)


class SlideshowBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = SlideshowBlock


class SlideshowFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Slideshow

    block = factory.SubFactory(SlideshowBlockFactory)

    @factory.post_generation
    def slideshow(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of products were passed in, use them
            for image in extracted:
                self.slideshow.add(image)

    @factory.sequence
    def order(n):
        return n


#class FeatureBlockFactory(factory.django.DjangoModelFactory):
#
#    page_section = factory.SubFactory(PageSectionFactory)
#
#    class Meta:
#        model = FeatureBlock
#
#
#class FeatureFactory(factory.django.DjangoModelFactory):
#
#    class Meta:
#        model = Feature
#
#    block = factory.SubFactory(FeatureBlockFactory)
#
#    @factory.sequence
#    def order(n):
#        return n
#
#
#class HeaderBlockFactory(factory.django.DjangoModelFactory):
#
#    page_section = factory.SubFactory(PageSectionFactory)
#
#    class Meta:
#        model = HeaderBlock
#
#
#class HeaderFactory(factory.django.DjangoModelFactory):
#
#    class Meta:
#        model = Header
#
#    block = factory.SubFactory(HeaderBlockFactory)
#
#    @factory.sequence
#    def order(n):
#        return n
