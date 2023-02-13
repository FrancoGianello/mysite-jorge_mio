from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic

class index(generic.ListView):
    context_object_name = "ultimasNoticias"
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class detalle(generic.DetailView):
    model = Question
    context_object_name = "encuesta"

class resultado(generic.DetailView):
    model = Question
    context_object_name = "encuesta"


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)

    try:
        selected_choice = question.options.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detalle.html', {
            'encuesta': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:resultado', args=(question.pk,)))
        return HttpResponseRedirect(reverse('polls:resultado', args=(question.id,)))
