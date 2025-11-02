from django.shortcuts import redirect

from skills.apps import SkillsConfig


def add_course(request):
    if request.method == 'POST':
        # Создание нового курса
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']  # Получение изображения
        SkillsConfig.objects.create(title=title, description=description, price=price, image=image)
        return redirect('index')  # Перенаправление на страницу каталога курсов
    return render(request, 'add_course.html')
