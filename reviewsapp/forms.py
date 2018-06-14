from django import forms

from . import models

class ReviewForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		super(ReviewForm, self).__init__(*args, **kwargs)
	class Meta:
		model = models.Reviews
		fields = ['user_name', 'review']
		widgets = {
			'user_name': forms.TextInput(attrs={'placeholder': 'Uw naam'}),
			'review': forms.Textarea(
				attrs={'placeholder': 'Wat vind je van onze diensten?'}),
		}
		labels = {
            'user_name': 'Naam',
			'rating': 'Beoordeling',
        }