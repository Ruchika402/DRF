from rest_framework.pagination import PageNumberPagination

class StudentPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'size'
    #ordering = 'id'  ordering pagination

#limit offset pagination
#class StudentPagination(LimitOffsetPagination):
   # default_limit = 3