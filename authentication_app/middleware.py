
class SampleMiddleware():
    def __init__(self, get_res):
        self.get_res = get_res
        
    def __call__(self, req):
        print("Middleware before req (view)")
        response = self.get_res(req)
        print("Middleware after res (view)")
        return response