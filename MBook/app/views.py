"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from models import *

Appname = 'Magic Book'

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'My contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'year':datetime.now().year,
        })
    )

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(Title__icontains=q)
        return render(
        request,
        'app/search.html',
        context_instance = RequestContext(request,
        {
            'books': books,
        })
    )
    else:
        return render(
        request,
        'app/search.html',
        context_instance = RequestContext(request,
        {
            'books': [],
        })
     )

def searchau(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(AuthorID__Name__icontains=q)
        return render(
        request,
        'app/searchau.html',
        context_instance = RequestContext(request,
        {
            'books': books,
        })
    )
    else:
        return render(
        request,
        'app/searchau.html',
        context_instance = RequestContext(request,
        {
            'books': [],
        })
     )

def addbook(request):
    errors = []
    ISBN = ""
    Title = ""
    Publisher = ""
    PublishDate = ""
    Price = ""
    AuthorID = ""
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(ISBN=q)
        if len(books) > 0:
            ISBN = books[0].ISBN
            Title = books[0].Title
            Publisher = books[0].Publisher
            PublishDate = books[0].PublishDate
            Price = books[0].Price
            AuthorID = books[0].AuthorID.AuthorID
    if request.method == "POST":
        if not request.POST.get('ISBN', ''):
            errors.append('Enter a ISBN.')
        else:
            ISBN = request.POST['ISBN']
        if not request.POST.get('Title', ''):
            errors.append('Enter a Title.')
        else:
            Title = request.POST['Title']
        if not request.POST.get('AuthorID', ''):
            errors.append('Enter a AuthorID.')
        else:
            AuthorID = request.POST['AuthorID']
        if request.POST.get('Publisher',''):
            Publisher = request.POST['Publisher']
        if request.POST.get('PublishDate',''):
            PublishDate = request.POST['PublishDate']
        if request.POST.get('Price',''):
            Price = request.POST['Price']
        if len(errors) == 0:
            nb = Book(ISBN=ISBN,Title=Title,AuthorID=Author.objects.get(AuthorID=AuthorID),Publisher=Publisher,PublishDate=PublishDate,Price=Price,ST=0)
            nb.save()
            ISBN = Title = AuthorID = Publisher = PublishDate = Price = "" 
    else:
        errors.append("请至少输入ISBN、Title和AuthorID")
    return render(
    request,
    'app/addbook.html',
    context_instance = RequestContext(request,
    {
        'errors': errors,
        'ISBN': ISBN,
        'Title': Title,
        'Publisher': Publisher,
        'PublishDate': PublishDate,
        'Price': Price,
        'AuthorID': AuthorID,
     })
    )

def addauthor(request):
    authorid = request.GET['q']
    found = []
    Name = ''
    Age = ''
    Country = ''
    saved = True
    author = Author.objects.filter(AuthorID=authorid)
    if len(author) > 0:
        found.append("")
        Name = author[0].Name
        Age = author[0].Age
        Country = author[0].Country
    if request.method == "POST":
        if request.POST.get('Name',''):
            Name = request.POST['Name']
        if request.POST.get('Age',''):
            Age = request.POST['Age']
        if request.POST.get('Country',''):
            Country = request.POST['Country']
        if (not Name == "") or (not Age == "") or (not Country == ""):
            au = Author(AuthorID=authorid,Name=Name,Age=Age,Country=Country)
            au.save()
            saved = False
    return render(
    request,
    'app/addauthor.html',
    context_instance = RequestContext(request,
    {
        'found': found,
        'seaid': authorid,
        'Name': Name,
        'Age': Age,
        'Country': Country,
        "saved": saved,
     })
    )

def deletebook(request):
    successed = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        book = Book.objects.get(ISBN=q)
        if book:
            book.delete()
            successed = True
    return render(
    request,
    'app/deletebook.html',
    context_instance = RequestContext(request,
    {
        'successed': successed,
    })
    )