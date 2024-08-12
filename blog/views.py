from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.utils import q_search
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Post


def blog(request):

    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)


    if order_by and order_by != "default":
        blog = blog.order_by(order_by)
    elif query:
        blog = q_search(query)
    else:
        blog = get_list_or_404(Post.objects.filter(status=1).order_by("created_on"))

    if order_by and order_by != "default":
        blog = blog.order_by(order_by)    

    paginator = Paginator(blog, 3)
    current_page_blog = paginator.page(int(page))

    context = {
        "title": "Blog - Блог",
        "blog": current_page_blog,
    
      
    }
    return render(request, "blog/index.html", context)

def post_detail(request, slug):
    template_name = "blog/post_detail.html"                                               
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
     
