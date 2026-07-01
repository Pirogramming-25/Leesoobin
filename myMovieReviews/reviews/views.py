from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
# Create your views here.

def review_list(request):
  sort = request.GET.get('sort', '-created_at')  # 기본 정렬은 최신순
  reviews = Review.objects.all().order_by(sort)
  return render(request,'reviews/review_list.html', {'reviews':reviews} )



def review_create(request):
  if request.method == 'POST':
    Review.objects.create(
        title=request.POST.get('title'),
        year=request.POST.get('year'),
        genre=request.POST.get('genre'),
        rating=request.POST.get('rating'),
        running_time=request.POST.get('running_time'),
        content=request.POST.get('content'),
        director=request.POST.get('director'),
        actors=request.POST.get('actors'),
    )
    return redirect('review-list')
  return render(request, 'reviews/review_form.html')

def review_detail(request, pk):
  review = get_object_or_404(Review, pk=pk)
  return render(request,'reviews/review_detail.html',{'review': review}  )




def review_update(request, pk):
  review = get_object_or_404(Review, pk=pk)
  if request.method == 'POST':
        review.title=request.POST.get('title')
        review.year=request.POST.get('year')
        review.genre=request.POST.get('genre')
        review.rating=request.POST.get('rating')
        review.running_time=request.POST.get('running_time')
        review.content=request.POST.get('content')
        review.director=request.POST.get('director')
        review.actors=request.POST.get('actors')
        review.save()
        return redirect('review-detail', pk=pk)
  return render(request, 'reviews/review_form.html', {'review': review})
        
    

def review_delete(request, pk):
  review = get_object_or_404(Review, pk=pk)
  review.delete()
  return redirect('review-list')
  