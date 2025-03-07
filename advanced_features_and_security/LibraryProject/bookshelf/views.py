
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .forms import ExampleForm

@require_http_methods(["GET"])
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
   
     return HttpResponse("Book list!")
