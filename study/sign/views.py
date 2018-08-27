# django的视图文件，控制向前端页面显示的内容
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    print(request.method)
    if request.method == "GET":
        id=request.GET.get("id")
        print(id)
        if id is None:
            return HttpResponse("请传入id")
        else:
            return HttpResponse("success, "+id)
# HttpResponse中引用了参数id，因此调用接口时未传入id参数时，会报空的错

#登录
def login(request):
    return HttpResponse(
    """
    <form>
    <p>用户名：</p>
    <input type="text"/><br>
    <p>密码：</p>
    <input type="password">
    </form>
    """)
def loginin(request):
    return render(request,"index.html")