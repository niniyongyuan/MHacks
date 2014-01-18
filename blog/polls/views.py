from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User  
from django.contrib.auth.decorators import login_required  
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout  
from django.template import RequestContext
from polls.form import RegistrationForm, LoginForm
from polls.models import Hacker
from datetime import datetime
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from polls.models import Choice, Poll

# all the informations needed for login and logout
def auth_view(request):  
    username=request.POST.get('login','')  
    password=request.POST.get('password','')  
    user=auth.authenticate(username=username,password=password)  
    if user is not None:  
        auth.login(request,user)  
        return HttpResponseRedirect('/polls/loggedin')  
    else:  
        return HttpResponseRedirect('/polls/invalid_login') 

def loggedin(request):  
    return render_to_response('polls/loggedin.html',  
            {'full_name':request.user.username})

def invalid_login(request):  
    return render_to_response('polls/invalid_login.html') 

def logout(request):  
    auth.logout(request)  
    return render_to_response('polls/logout.html')  

def register(request): 
    if (request.user.is_authenticated()):
        return HttpResponseRedirect('/polls/loggedin') 

    if request.method =='POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            user =User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],password=form.cleaned_data['password'])  
            user.save()  
            hacker=Hacker(user=user,name=form.cleaned_data['name'],birthday=form.cleaned_data['birthday'])  
            hacker.save()  
            return HttpResponseRedirect('/polls/loggedin')  
        else:
            return render_to_response('polls/register.html',{'form':form},context_instance=RequestContext(request))  
    else: 
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('polls/register.html',context, context_instance = RequestContext(request)) 


'''@login_required  
def profile(request):  
    if not request.user.is_authenticated():  
        return HttpResponseRedirect('/')  
    hacker=request.user.get_profile() 
    context={'hacker':hacker}  
    return render_to_response('polls/profile.html',context,context_instance=RequestContext(request))  
'''


def loginRequest(request):
    #if request.user.is_authenticated():  
     #   return HttpResponseRedirect('/polls/login')  
    if request.method == 'POST':  
        form=LoginForm(request.POST)  
        if form.is_valid():  
            username=form.cleaned_data['username']  
            password=form.cleaned_data['password']  
            hacker=authenticate(username=username,password=password)  
            if hacker is not None:  
                login(request,hacker)  
                return HttpResponseRedirect('/polls/')  
            else:  
                return render_to_response('polls/invalid_login.html',{'form':form},context_instance=RequestContext(request))  
        else:  
            return render_to_response('polls/invalid_login.html',{'form':form},context_instance=RequestContext(request))  
    else:  
        form=LoginForm()  
        context={'form':form}  
        return render_to_response('polls/login.html',context,context_instance=RequestContext(request))  

'''def register_success(request):  
    if not request.user.is_authenticated():  
        return HttpResponseRedirect('polls/login/')  
    hacker=request.user.get_profile  
    context={'Hacker': hacker}  
    return render_to_response('polls/register_success.html', context, context_instance=RequestContext(request))
'''

# after login, the user can view the questionare
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))