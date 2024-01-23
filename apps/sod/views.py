from django.shortcuts import render,redirect

def home_view(request):
    if request.method == 'POST':
        pass
    else:
        if request.session['token'] is None:
            return redirect('apps.accounts:login')
        else:
            token = request.session['token']
            return render(request, 'sod/index.html')
