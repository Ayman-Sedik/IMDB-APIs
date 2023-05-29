from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination



class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'

    # customize the size of page to load results
    page_size_query_param = 'size'
    max_page_size = 10
    # get last page
    last_page_strings = 'last'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 7
    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'
