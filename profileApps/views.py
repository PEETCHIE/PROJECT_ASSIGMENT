from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Home.html")

def personalRecord(request):
    return render(request, "personalRecord.html")

def educationRecord(request):
    return render(request, "educationRecord.html")

def interests(request):
    return render(request, "interests.html")

def productsale(request):
    return render(request, "productsale.html")

def roleModel(request):
    return render(request, "roleModel.html")

def showMyData(request):
    id = "RMUTI65342310224"
    fname = "Chaianan"
    lname = "Simachai"
    nickname = "Peet"
    gender = "ชาย"
    status = "นักศึกษา"
    education = "ปริญญาตรี"
    vehicle = "Honda WAVE"
    telephone = "Samsung Galaxy J8"
    laptop = "Lenovo Ideapad gaming 3"
    productList = [["Air Force 1 '07", 3700, 'static/images/Air Force 1 07.jpg'],
                   ["VANS OLD SKOOL - BETTER NATURE GRAY", 2900, 'static/images/vans.jpg'],
                   ["SB Zoom Blazer Low Pro GT", 2900, 'static/images/sbblazerlowprogt.jpg'],
                   ["SB Dunk High Pro PRM", 4300, 'static/images/SB Dunk High Pro PRM.jpg'],
                   ["HIBISCUS CHECK BLACK", 3100, 'static/images/HIBISCUS CHECK BLACK.jpg'],
                   ["VANS CLASSIC SLIP-ON - BLACK", 2090, 'static/images/VANS CLASSIC SLIP-ON - BLACK.jpg'],
                   ["VANS OLD SKOOL - NAVY", 2490, 'static/images/VANS OLD SKOOL - NAVY.jpg'],
                   ["EL DISTRITO 2.0 SEASONAL COLOR OX YELLOW", 2100, 'static/images/EL DISTRITO 2.0 SEASONAL COLOR OX YELLOW.jpg'],
                   ["CHUCK 70 SPRING COLOR HI GREY", 3000, 'static/images/CONVERSE CHUCK 70 SPRING COLOR HI GREY.jpg'],
                   ["Jack Purcell", 2600, 'static/images/CONVERSE Jack Purcell.jpg']
                   ]

    return render(request, 'showMyData.html', {'id': id, 'fname': fname, 'lname': lname, 'nickname': nickname, 'gender': gender,
                                               'status': status, 'education': education, 'vehicle': vehicle, 'telephone': telephone,
                                               'laptop': laptop, 'productList':productList})



