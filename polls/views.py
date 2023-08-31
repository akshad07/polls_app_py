from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Delete
from django.utils import timezone
from django.http import HttpResponseRedirect
from polls.forms import QuestionForm , deleteForm1
from django.shortcuts import render, redirect



    
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



def add_que(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            q = Question()
            q.question_text= form.cleaned_data["Question"]
            q.pub_date= timezone.now()
            q.save()
            c1 =Choice(question=q)
            c1.choice_text = form.cleaned_data["Choice1"]
            c1.save()
            c2 = Choice(question = q)
            c2.choice_text = form.cleaned_data["Choice2"]
            c2.save()
            form = QuestionForm()


    else:
        form = QuestionForm()

    return render(request, "polls/question.html", {"questionform": form})
    

def delete1(request):
    if request.method == "POST":
        form = deleteForm1 (request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            q= form.cleaned_data["Question_ID_"]
            d=Question.objects.get(id=q)
            d.delete()
            form = deleteForm1()


    else:
        form = deleteForm1()

    return render(request, "polls/delete.html", {"deleteForm1": form})
