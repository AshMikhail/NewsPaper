from django_filters import FilterSet, ModelMultipleChoiceFilter
from django_filters import DateFilter
from django.forms import DateInput
from .models import Post, Category


class PostFilter(FilterSet):
    postCategory = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
    )

    added_after = DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'postCategory': ['exact'],
        }
