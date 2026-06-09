from rest_framework.throttling import UserRateThrottle

class StudentThrottle(UserRateThrottle):
    rate = '10/hr'