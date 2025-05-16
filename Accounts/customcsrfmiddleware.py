class CustomCsrfMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    

    def __call__(self,request):
        paths= request.path
        csrf_exempt_paths=[
            paths
        ]
        
        if request.path in csrf_exempt_paths:
            setattr(request,'_dont_enforce_csrf_checks',True)
        
        return self.get_response(request)