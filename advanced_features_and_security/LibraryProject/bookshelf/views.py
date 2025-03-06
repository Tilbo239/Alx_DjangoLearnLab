from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('bookshelf.can_view', raise_exception=True)
def comment_list(request):
   
     return HttpResponse("You can view the books!")

@permission_required('bookshelf.can_create', raise_exception=True)
def create_comment(request):
    return HttpResponse("You can create a comment!")
    

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_comment(request, comment_id):
    return HttpResponse("Post updated!")
    

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_comment(request, comment_id):
    return HttpResponse("Post deleted!") 
