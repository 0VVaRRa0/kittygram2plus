from datetime import datetime

from rest_framework.throttling import BaseThrottle


class WorkingHoursRateThrottle(BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.now().hour
        if now >= 22 and now < 7:
            return False
        return True
