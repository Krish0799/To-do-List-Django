from django.shortcuts import render,redirect
from ToDoLi.models import Task
from ToDoLi.models import CompletedTask
from ToDoLi.forms import TaskForm

# Create your views here.

def display_Tasks(request):
	# cmt-----
	# cmt --added by kk
	tsk = Task.objects.all()
	return render(request,'ToDoLi/index.html',{'task':tsk})
	
def create_view(request):
	tsk = TaskForm()
	if request.method=="POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'ToDoLi/create.html',{'form':tsk})
		
	
def update_view(request,id):
	tsk = Task.objects.get(id=id)
	if request.method == "POST":
		form = TaskForm(request.POST,instance = tsk)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'ToDoLi/update.html',{'task':tsk})

def delete_view(request,id):
	try:
		ctsk = CompletedTask.objects.get(id=id)
		if ctsk:
			ctsk.delete()
			return redirect('/completed')
	except CompletedTask.DoesNotExist:
		tsk = Task.objects.get(id=id)
		tsk.delete()
	return redirect('/')
	
def markdone_view(request,id):
	tsk = Task.objects.get(id=id)
	ctsk = CompletedTask.objects.create(ctname = tsk.tname,ctDetails = tsk.tDetails)
	ctsk.save()
	tsk.delete()
	return redirect('/')
def completed(request):
	ctsk = CompletedTask.objects.all()
	return render(request,'ToDoLi/completed.html',{'ctask':ctsk})