from django.shortcuts import render

# CSyang
def post_list(request):
	return render(request, 'blog/post_list.html', {})
	