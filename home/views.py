from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "index.html")

def index(request):
   # now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse("html")