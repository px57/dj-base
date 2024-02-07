from django.shortcuts import render
from kernel.http.response import Response

def info(request):
    """
        @description:
    """
    res = Response(request=request)
    return res.success()