
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
   
     return HttpResponse("Book list!")
