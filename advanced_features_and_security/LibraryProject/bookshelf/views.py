
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
   
     return HttpResponse("Book list!")

@permission_required('bookshelf.can_view', raise_exception=True)
def post_list(request):
   
     return HttpResponse("Post list!")

@permission_required('bookshelf.can_create', raise_exception=True)
def create_post(request):
    return HttpResponse("Post created!")
    

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_post(request, article_id):
    return HttpResponse("Post updated!")
    

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_post(request, article_id):
    return HttpResponse("Post deleted!") 
