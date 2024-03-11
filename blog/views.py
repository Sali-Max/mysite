from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import *
import platform, psutil
# Create your views here.


def home(request):
    return render(request, "home.html")


###########################################################################


def list(request):
    allPosts = Post.objects.filter(status=True) #Get Public Posts

    context = {
    'posts' : allPosts  # Send Public Posts
    }
    return render(request, "list.html", context)

########################################################################


def addPost(request):
    Form = PostForm()
    if request.method == "POST":
        Form = PostForm(request.POST)
        if Form.is_valid():
            cd = Form.cleaned_data
            OBJ = Post.objects.create(name=cd['name'],text=cd['text'],
                                      user = request.user, read_time=cd['read_time']
                                      )
            return redirect('blog:home')



    context = {
        'form' : Form
    }
    return render(request,'addPost.html', context)


def postView(request,id):
    POST = get_object_or_404(Post,id=id,status=True)    #Get post with id And public
    context = {
        'post' : POST
    }
    return render(request, 'show_post.html', context)

def serverInfo(request):


    system = platform.system
    release = platform.release(); version = platform.version()
    version = version.split(" ")[5]

    all_RAM = round((psutil.virtual_memory()[0])/1000000000)
    used_ram = round((psutil.virtual_memory()[3]) / 1000000000)

    cpu = psutil.cpu_count()
    cpuf = round(psutil.cpu_freq()[2])

    
    context = {
        'system' : system,
        'release' : release,
        'version' : version,
        'ram' : all_RAM,
        'useRam' : used_ram,
        'cpu' : cpu,
        'cpuf' : cpuf
    }
    return render(request, 'server_info.html', context)
