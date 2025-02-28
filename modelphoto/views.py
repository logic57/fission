from django.shortcuts import render

def model_photo_maker(request):
    """模特图制作页面的视图函数"""
    return render(request, 'modelphoto/model_photo_maker.html')