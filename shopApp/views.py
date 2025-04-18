from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopApp.models import Product, Contact
from shopApp.forms import FormComment, FormContact

def index(request):
    #return HttpResponse("Hola mundo desde Django!")
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer = True)

    my_context = {
        'message' : "Haces un buen trabajo :)",
        'product_list': product_list,
        'special_offers': special_offers,
        'special_offers_2': [ 
            {"nombre": "Mascarilla hidratante de savila","precio": 14.00,"img":"https://cosmos-beauty.mx/cdn/shop/products/mascarilla-facial-cactus.jpg?v=1677525335&width=1500"},
            {"nombre": "Consla de videojuegos retro portatil","precio": 254.00,"img":"https://m.media-amazon.com/images/I/41lB0Mx4XuL.jpg"},
            {"nombre": 'Reloj de pulsera de snoopy',"precio": 10.50,"img":"https://m.media-amazon.com/images/I/81hiL2BX-rL.jpg"},
            {"nombre": 'Camisa para caballero de algodon',"precio": 140.00,"img":"https://milano.com/cdn/shop/products/866-710533A2_Camisa_Casual_Lisa_Manga_Corta_.Caballero_Milano_A_250x.jpg?v=1627434094"},
            {"nombre": 'Peluche de batman tamaño real',"precio": 200.00,"img":"https://i5.walmartimages.com/asr/52abb7a8-0c72-4dc2-9df4-80c36a0ba5a2.f240c36a7be743558261875a4154d6bf.webp?odnHeight=612&odnWidth=612&odnBg=FFFFFF"},
            ],
        "featured_products":[
            {"nombre":"Figura de Accion de Superman","precio":120.99,"img":"https://detqhtv6m6lzl.cloudfront.net/HCLContenido/producto/FullImage/681147015449-1.jpg"},
            {"nombre":"Face shell para mascara","precio":300.00,"img":"https://m.media-amazon.com/images/I/61-NjVP8nJL.jpg"},
            {"nombre":"Reloj de Ben 10","precio":20.00,"img":"https://m.media-amazon.com/images/I/41kpsBgN98L._AC_SY580_.jpg"},
            {"nombre":"Disfraz de flash (superheroe)","precio":120.99,"img":"https://http2.mlstatic.com/D_NQ_NP_777513-MLM70350686581_072023-O.webp"},
            {"nombre":"Patineta de Shrek","precio": 250.99,"img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrDHzY--9ngAwP0Hx5Uv21qC09TU_q-pCi-Q&s"},
        ],
    }

    return render(request, "shopApp/index.html", context = my_context)

def about(request):
    active_contacts = Contact.objects.filter(contact_active = True).order_by('contact_full_name')
    my_context = {
        "contacts": active_contacts,
    }
    return render(request, "shopApp/about.html", context = my_context)

def form_comment(request):
    form = FormComment()

    if request.method =="POST":
        form = FormComment(request.POST)
        if form.is_valid():
            print('formulario valido')
            print('Nombre: ', form.cleaned_data['full_name'])
            print('Email: ', form.cleaned_data['email'])
            print('Comment', form.cleaned_data['comment'])
    return render(request, 'shopApp/form_comment.html', context = { 'form': form })

def form_contact(request):
    form = FormContact()

    if request.method == "POST":
        form = FormContact(request.POST)
        if form.is_valid():
            contact = Contact.objects.get_or_create(
            contact_full_name =form.cleaned_data['full_name'],
            contact_address = form.cleaned_data['address'],
            contact_phone = form.cleaned_data['phone'],
            contact_email = form.cleaned_data['email'],
            contact_active = form.cleaned_data['contact_active']
            )
            return redirect(to = 'about')
    else:
        form = FormContact()

    return render(request, 'shopApp/form_contact.html', context = { 'form': form })