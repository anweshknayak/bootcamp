from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from bootcamp.activities.models import Notification
from bootcamp.decorators import ajax_required


@login_required
class Notifications(View):
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(to_user=user)
        unread = Notification.objects.filter(to_user=user, is_read=False)
        for notification in unread:
            notification.is_read = True
            notification.save()

        return render(request, 'activities/notifications.html',
                      {'notifications': notifications})


@login_required
@ajax_required
class Last_notifications(View):
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(to_user=user,
                                                is_read=False)[:5]
        for notification in notifications:
            notification.is_read = True
            notification.save()

        return render(request, 'activities/last_notifications.html',
                       {'notifications': notifications})


@login_required
@ajax_required
class Check_notifications(request):
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(to_user=user,
                                                is_read=False)[:5]
        return HttpResponse(len(notifications))
