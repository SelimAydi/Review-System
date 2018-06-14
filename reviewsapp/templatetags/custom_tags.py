from django import template
from ..models import Reviews
from django.db.models import Avg

register = template.Library()

@register.simple_tag
def getStars(num):
	result = ""
	for i in range(num):
		result += "<i class='fas fa-star' style='color: #b8f789;'></i>"
	return result

@register.simple_tag
def getAmountofReviews():
	return Reviews.objects.all().count()

@register.simple_tag
def getAverage():
	rating = Reviews.objects.aggregate(Avg('rating'))['rating__avg']
	return "{0:0.1f}".format(rating)

@register.simple_tag
def showButton():
	print("total amount: " + str(getAmountofReviews()))
	if Reviews.objects.all().count() < 1:
		return ""
	return "<a id='back' href='/'>Review plaatsen</a>"

@register.simple_tag
def getAvgStars():
	if Reviews.objects.all().count() < 1:
		return "<p class='noreviews'> Op dit moment zijn er nog geen reviews. Wilt u de eerste zijn? </p><a href='/' id='back' style='left: 0; right: 0; margin: 2vh auto;'>Plaats een review</a>"
	
	num = float(getAverage())	
	html =	"""
			<div class="avg">
				<p>Gemiddelde score:</p>
				{0}
				<p>{1}</p>
				</div>
			""".format(getStars(round(num)), getAverage())
	return html
