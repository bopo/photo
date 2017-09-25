# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.vary import vary_on_headers
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from django.utils.http import urlquote, urlunquote
from .models import Category, Tags
from .models import *


def navigation():
    return Category.objects.all().values('id', 'title', 'slug')


# @cache_page(60 * 15)
def home(request):
    # if request.mobile:
    #     print request.COOKIES, request.POST

    recommend = Photo.objects.order_by('-id').filter(recommend=1).all()[:10]
    photos = Photo.objects.order_by(
        '-id').filter(cover__startswith='cover/').all()[:20]
    weblink = Weblink.objects.all()
    category = Category.objects.all()
    cat_list = []
    menu = navigation()
    home = 1

    for x in category:
        x.photos = x.photo_set.order_by('-id').all()[:8]
        # .values('id','title','cover','pub_date','likes','views','tags')
        cat_list.append(x)

    return render(request, 'index.html', locals())


@cache_page(60 * 15)
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    photo_list = category.photo_set.order_by('-id').all()
    paginator = Paginator(photo_list, 20)
    page = request.GET.get('page')

    print(slug)

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    menu = navigation()
    return render(request, 'category.html', locals())


@cache_page(60 * 15)
def detail(request, id):

    try:
        photo = Photo.objects.get(pk=id)
        weblink = Weblink.objects.all()
        category = photo.category.all()[0]
    except Photo.DoesNotExist:
        raise Http404

    # context = {'tags': tags, 'photo': photo, 'menu': navigation(), 'category': category}

    menu = navigation()       
    return render(request, 'detail.html', locals())

# @vary_on_headers('User-Agent', 'Cookie')


@cache_page(60 * 15)
def new(request):
    recommend = Photo.objects.order_by('-id').filter(recommend=1).all()[:10]
    photos = Photo.objects.order_by(
        '-id').filter(cover__startswith='cover/').all()[:20]
    context = {'freeID': 0, 'title': '最新', 'photos': photos,
               'menu': navigation(), 'recommend': recommend, }
    
    return render(request, 'flatpages.html', context)


@cache_page(60 * 15)
def rec(request):
    recommend = Photo.objects.order_by('-id').filter(recommend=1).all()[:10]
    photos = Photo.objects.order_by(
        '-id').filter(cover__startswith='cover/').all()[:20]
    context = {'freeID': 1, 'title': '精选', 'photos': photos,
               'menu': navigation(), 'recommend': recommend, }
    return render(request, 'flatpages.html', context)


@cache_page(60 * 15)
def hot(request):
    recommend = Photo.objects.order_by('-id').filter(recommend=1).all()[:10]
    photos = Photo.objects.order_by(
        '-id').filter(cover__startswith='cover/').all()[:20]
    context = {'freeID': 2, 'title': '热门', 'photos': photos,
               'menu': navigation(), 'recommend': recommend, }
    return render(request, 'flatpages.html', context)


@cache_page(60 * 15)
def tags(request, name):
    page = int(request.GET.get('page', 1))
    tags = get_object_or_404(Tag, title=name)

    photo_list = tags.photo_set.all()
    paginator = Paginator(photo_list, 20)

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = {'tags': tags, 'photos': photos, 'menu': navigation()}
    return render(request, 'tags.html', context)


@cache_page(60 * 15)
def search(request):
    size = int(request.GET.get('pagesize', 20))
    page = int(request.GET.get('page', 1))
    word = request.GET.get('keyword')

    photo_list = Photo.objects.filter(title__contains=word)
    paginator = Paginator(photo_list, int(size))

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = {'keyword': keyword, 'photos': photos, 'menu': navigation()}
    return render(request, 'search.html', context)


@cache_page(60 * 15)
def waterfall(request, id):
    try:
        page = int(request.GET.get('page', 1))
        photo_list = Photo.objects.filter(cover__startswith='cover/')

        if id == 1:
            photo_list.order_by('-likes')
        elif id == 2:
            photo_list.order_by('-id').filter(recommend=1)
        else:
            photo_list.order_by('-id')

        paginator = Paginator(photo_list, 12)
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    return render(request, 'slide.html', {'photos': photos})


def slide(request, swith, id):

    page = int(request.GET.get('page', 1))

    if swith == 'data':
        try:
            import json
            photo = Photo.objects.get(pk=id)
            next = Photo.objects.order_by('id').filter(
                id__gt=id).values('id', 'title', 'cover')[:1]
            prev = Photo.objects.order_by(
                '-id').filter(id__gt=id).values('id', 'title', 'cover')[:1]

            slide_data = {}
            slide_data['slide'] = {
                'title': photo.title,
                'createtime': '',
                'click': photo.get_absolute_url(),
                'like': photo.likes,
                'url': photo.get_absolute_url(),
            }

            i = 1
            slide_data['images'] = []
            slide_data['next_album'] = {
                "interface": "",
                "title": next[0]['title'],
                "url": '/detail/%s' % next[0]['id'],
                "thumb_50": '/media/' + next[0]['cover'],
            }

            slide_data['prev_album'] = {
                "interface": "",
                "title": prev[0]['title'],
                "url": '/detail/%s' % prev[0]['id'],
                "thumb_50": '/media/' + prev[0]['cover'],
            }

            for x in json.loads(photo.photolist):
                images = {
                    'title': '',
                    'intro': '',
                    'comment': '',
                    'width': '',
                    'height': '',
                    'thumb_50': x,
                    'thumb_160': x,
                    'image_url': x,
                    'source': '',
                    'id': i,
                }

                i += 1

                slide_data['images'].append(images)
            return HttpResponse('var slide_data = ' + json.dumps(slide_data))
        except Exception:
            pass

    elif swith == 'count':
        photo = Photo.objects.get(pk=id)
        photo.views = photo.views + 1
        photo.save()
        return HttpResponse("%s" % photo.views)
    elif swith == 'like':
        photo = Photo.objects.get(pk=id)
        return HttpResponse("%s" % photo.likes)
    elif swith == 'upclike':
        photo = Photo.objects.get(pk=id)
        photo.likes = photo.likes + 1
        photo.save()
        return HttpResponse("%s" % photo.likes)
    else:
        pass
