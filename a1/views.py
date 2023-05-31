from django.shortcuts import render,redirect
from .models import ImageList,PostNews,VideoList, PostCompetition,ImageList1,VideoList1
# Create your views here.

def competitionOut(request):
    poccets = []
    allPost = PostCompetition.objects.all()
    for i in allPost:
        poccet = {}
        poccet.update({'created':i.created_time})
        poccet.update({'title':i.title})
        print(type(i.title))
        poccet.update({'body':i.body})
        imgs = ImageList1.objects.filter(which_Post=i)
        print(type(imgs))
        poccet.update({'images':imgs})
        videos = VideoList1.objects.filter(which_Post=i)
        poccet.update({'videos':videos})
        poccets.append(poccet)
    context = {
        'poccets':poccets
    }
    return render(request, 'competition.html', context)

def newsOut(request):
    poccets = []
    allPost = PostNews.objects.all()
    for i in allPost:
        poccet = {}
        poccet.update({'created':i.created_time})
        poccet.update({'title':i.title})
        print(type(i.title))
        poccet.update({'body':i.body})
        imgs = ImageList.objects.filter(which_Post=i)
        print(type(imgs))
        poccet.update({'images':imgs})
        videos = VideoList.objects.filter(which_Post=i)
        poccet.update({'videos':videos})
        poccets.append(poccet)
    context = {
        'poccets':poccets
    }
    return render(request, 'newsOut.html', context)
    

def uploadN(request):
    if request.method == 'POST':
       if request.POST.get('title')!=None and len(request.POST.get('title'))!=0:
           title = request.POST.get('title')
           body = request.POST.get('body')
           images = request.FILES.getlist('images')
           videos = request.FILES.getlist('videos') 
           post = PostNews.objects.create(
                title=title,
                body=body,
            )
           which_Post = post
           if images!=None:
             for i in images:
                ImageList.objects.create(
                which_Post=which_Post,
                images = i,
                )
           if videos!=None:
              for i in videos:
                 VideoList.objects.create(
                    which_Post=which_Post,
                    video = i,
                )

       if request.POST.get('title1')!=None and len(request.POST.get('title1'))!=0:
           title = request.POST.get('title1')
           body = request.POST.get('body1')
           images = request.FILES.getlist('images1')
           videos = request.FILES.getlist('videos1') 
           post = PostCompetition.objects.create(
                    title=title,
                    body=body,
            )
           which_Post = post
           if images!=None:
             for i in images:
                ImageList1.objects.create(
                which_Post=which_Post,
                images = i,
                )
           if videos!=None:
              for i in videos:
                 VideoList1.objects.create(
                    which_Post=which_Post,
                    video = i,
                )        

       return redirect('home')     
       
    context = {}
    return render(request, 'upload.html', context)

def home(request):
    context = {}
    return render(request, 'index.html', context)