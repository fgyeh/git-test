from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        # 用户名不能重复
        res = models.User.objects.filter(username=username).exists()
        if not res:
            if password == re_password:
                # 保存数据到数据库
                models.User.objects.create(username=username, password=password)
                return redirect('/login/')
            else:
                return HttpResponse('两次密码不一致')
        else:
            return HttpResponse('用户名已存在')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 判断用户名和密码是否符合数据库的数据
        user_obj = models.User.objects.filter(username=username, password=password).first()
        if user_obj:
            return redirect('/home/')
        else:
            return HttpResponse('用户名或密码错误')
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def book_list(request):
    book_queryset = models.Book.objects.filter(is_delete=False)
    return render(request, 'book_list.html', locals())


def book_add(request):
    publish_queryset = models.Publish.objects.filter(is_delete=False)
    author_queryset = models.Author.objects.filter(is_delete=False)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish_id = request.POST.get('publish_id')
        authors = request.POST.getlist('author')  # [1, 2]
        # 操作数据库添加图书
        book_obj = models.Book.objects.create(title=title,
                                              price=price,
                                              publish_date=date,
                                              publish_id=publish_id)

        book_obj.authors.add(*authors)
        # *列表/*元祖:可以将列表/元祖当做位置参数传给函数
        # add(*[1, 2])--->age(1, 2)
        # **字典:将字典当做关键字参数传给函数
        # create(**{'name':'xixi', 'age': 18})--->create(name='xixi', age=18)
        return redirect('book_list')
    return render(request, 'book_add.html', locals())


def book_edit(request, edit_id):
    # 通过id获取到要编辑的书对象
    book_obj = models.Book.objects.filter(id=edit_id).first()
    publish_queryset = models.Publish.objects.filter(is_delete=False)
    author_queryset = models.Author.objects.filter(is_delete=False)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish_id')
        authors = request.POST.getlist('author')
        models.Book.objects.filter(id=edit_id).update(title=title,
                                                      price=price,
                                                      publish_id=publish_id)
        book_obj.authors.set(authors)  # set括号传入可迭代对象
        return redirect('book_list')
    return render(request, 'book_edit.html', locals())


def book_delete(request, delete_id):
    # 如果直接调用delete删除书,不会影响出版社, 但是书对应的作者信息会删除
    models.Book.objects.filter(id=delete_id).update(is_delete=True)
    return redirect('book_list')


def publish_list(request):
    publish_queryset = models.Publish.objects.filter(is_delete=False)
    return render(request, 'publish_list.html', locals())


def publish_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        models.Publish.objects.create(name=name, addr=addr)
        return redirect('publish_list')
    return render(request, 'publish_add.html')


def publish_edit(request, edit_id):
    publish_obj = models.Publish.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        publish_obj.name = name
        publish_obj.addr = addr
        publish_obj.save()
        return redirect('publish_list')
    return render(request, 'publish_edit.html', locals())


def publish_delete(request, delete_id):
    models.Publish.objects.filter(id=delete_id).update(is_delete=True)
    return redirect('publish_list')


def author_list(request):
    author_queryset = models.Author.objects.filter(is_delete=False)
    return render(request, 'author_list.html', locals())


def author_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')
        # 先创建作者详情,再创建作者
        author_detail_obj = models.AuthorDetail.objects.create(phone=phone, addr=addr)
        models.Author.objects.create(name=name, age=age, email=email, author_detail=author_detail_obj)
        return redirect('author_list')
    return render(request, 'author_add.html')


def author_edit(request, edit_id):
    author_obj = models.Author.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')
        # 直接修改,不需要考虑顺序
        models.Author.objects.filter(id=edit_id).update(name=name, age=age, email=email)
        # 或者获取作者详情
        models.AuthorDetail.objects.filter(author__id=edit_id).update(phone=phone, addr=addr)
        # author_obj.author_detail.phone = phone
        # author_obj.author_detail.addr = addr
        # author_obj.author_detail.save()
        return redirect('author_list')
    return render(request, 'author_edit.html', locals())


def author_delete(request, delete_id):
    models.Author.objects.filter(id=delete_id).update(is_delete=True)
    models.AuthorDetail.objects.filter(author__id=delete_id).update(is_delete=True)
    return redirect('author_list')