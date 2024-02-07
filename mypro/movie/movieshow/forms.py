
from django import forms

from movieshow.models import movieshow


class movieform(forms.ModelForm):
    class Meta:
        model = movieshow
        fields = "__all__"
