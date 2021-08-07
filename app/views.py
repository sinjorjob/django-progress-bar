from django.shortcuts import render
from django.views.generic import View
from app.forms import FileUploadForm
from django.http import JsonResponse


class FileUploadView(View):

    def get(self, request):
        
        form = FileUploadForm()
        return render(request, 'home.html', context={'form':form})

    def post(self, request):
        if request.method=='POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return JsonResponse({'data':'ファイルのアップロードが完了しました。'})

            else:
                return JsonResponse({'data':'アップロード処理でエラーが発生しました。'})