from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core.models import Business
from .models import Review

@login_required
def add_review(request, business_id):
    if request.method == 'POST':
        business = get_object_or_404(Business, id=business_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if rating and comment:
            review, created = Review.objects.get_or_create(
                business=business,
                user=request.user,
                defaults={'rating': rating, 'comment': comment}
            )
            
            if not created:
                review.rating = rating
                review.comment = comment
                review.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Review added successfully!',
                'rating': review.rating,
                'comment': review.comment,
                'user': request.user.username
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

@login_required
def business_reviews(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    reviews = Review.objects.filter(business=business)
    
    context = {
        'business': business,
        'reviews': reviews
    }
    return render(request, 'reviews/business_reviews.html', context)