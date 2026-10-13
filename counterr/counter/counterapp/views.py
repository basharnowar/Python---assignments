from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    elif 'count' not in request.session:
        request.session['count'] = 0
        return render(request, "index.html")

    return render(request, "index.html")

def destroy_session(request):
    request.session.flush()
    return redirect('/')