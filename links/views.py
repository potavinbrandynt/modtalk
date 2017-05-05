from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import LinkForm, UserProfileForm, VoteForm
from .models import Link, UserProfile, Vote

from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse, reverse_lazy

class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 5
    
class LinkDetailView(DetailView):
    model = Link
    
class  LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()
        return super(LinkCreateView, self).form_valid(form)

class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm
    
class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy("home")
    
class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"
    
    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "edit_profile.html"
    
    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]
        
    def get_success_url(self):
        return reverse("profile", kwargs={"slug": self.request.user})

class VoteFormView(FormView):
    model = Vote
    form_class = VoteForm
    template_name = "link_list.html"
    
    def form_valid(self, form):
        link = get_object_or_404(Link, pk=form.data["link"])
        user = self.request.user
        prev_votes = Vote.objects.filter(voter=user, link=link )
        has_voted = (prev_votes.count() > 0)
        
        if not has_voted:
            #add vote
            Vote.objects.create(voter=user, link=link)
            print("voted")
        else:
            # delete vote
            prev_votes[0].delete()
            print("unvoted")
        return redirect("home")
            
    def form_invalid(self, form):
        print("invalid")
        return redirect("home")