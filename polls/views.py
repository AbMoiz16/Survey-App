from django.shortcuts import render
from .models import Question, Choice, Comment
from .forms import CommentForm


# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html',{'questions': questions})

def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    comment = question.comments.all() # get comments from database comment to show in vote page 
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = question
            new_comment.save()
    else:
        form = CommentForm()


    if request.method == 'POST':
        inputvalue =  request.POST['choice']
        selection_option = options.get(id=inputvalue) 
        selection_option.vote += 1
        selection_option.save()

    return render(request, 'vote.html',{'question': question, 'options': options, 'form': form, 'new_comment': new_comment, 'comment': comment})

def result(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    comment = question.comments.all() # get comments from database comment to show in vote page 
    new_comment = None

    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 1
        selection_option.save()

    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = question
            new_comment.save()
    else:
        form = CommentForm()

    return render(request, 'result.html',{'question': question, 'options': options, 'form': form, 'new_comment': new_comment, 'comment': comment})

    
