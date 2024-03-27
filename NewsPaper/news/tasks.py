from celery import shared_task

import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from news.models import Post, Subscriber

@shared_task
def monday_mail_task():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscribers = set(User.objects.filter(subscriptions__category__name__in=categories).values_list('email', flat=True))

    html_content = render_to_string(
        'weekly_post.html',
    {
        'link': settings.SITE_URL,
        'posts': posts,

    }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю!',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def new_post_email(pk):
    post = Post.objects.get(pk=pk)
    subscribers_emails = User.objects.filter(subscriptions__category__in=post.postCategory.all()).values_list('email',
                                                                                                              flat=True)
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': post.preview,
            'link': f'http://127.0.0.1:8000/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()