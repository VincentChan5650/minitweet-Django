from rest_framework import pagination

class standardResultsPagination(pagination.PageNumberPagination):
    page_size = 10 #default page size
    page_size_query_param = 'page_size'
    max_page_size = 1000
