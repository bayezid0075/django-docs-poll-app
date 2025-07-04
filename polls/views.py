from django.shortcuts import render
from django.http import HttpResponse as htr
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return htr(template.render(context, request))

def detail(request, question_id):
    return htr("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return htr(response % question_id)


def vote(request, question_id):
    return htr("You're voting on question %s." % question_id)