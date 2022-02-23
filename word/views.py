from django.shortcuts import render
from .models import Score
# Create your views here.

def add_word(request):
	score ={'a':1,'b':1,'c':1,'d':1,'e':1,'f':2,'g':2,'h':2,'i':2,'j':2,'k':3,'l':3,'m':3,'n':3,'o':3,'p':4,'q':4,'r':4,'s':4,'t':4,'u':5,'v':5,'w':5,'x':5,'y':5,'z':1}
	sum_score=0
	if request.method=='POST':
		word = request.POST.get('word')
		data_list= [score[w] for w in word]
		sum_score=sum(data_list)
		Score.objects.create(input_str=word,sum_score=sum_score)
	return render(request,'add_word.html',{'sum_score':sum_score})

def list_scores(request):
	scores = Score.objects.all()

	return render(request,'list_scores.html',{'scores':scores})
