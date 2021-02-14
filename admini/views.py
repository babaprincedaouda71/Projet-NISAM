from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from admini.models import Member, Treasury, Reunion
from admini.forms import memberForm, treasuryForm, meetingForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def adminBase(request):
    return render(request, 'admini/adminBase.html')



def login(request):
    return render(request, 'admini/login.html')


@login_required
def newMember(request):
    submitted = False
    if request.method == 'POST':
        form = memberForm(request.POST, request.FILES)
        if form.is_valid():
            amci = request.POST['amci']
            fname = request.POST['fname']
            lname = request.POST['lname']
            mail = request.POST['mail']
            date_nais = request.POST['date_nais']
            tel = request.POST['tel']
            annee_bourse = request.POST['annee_bourse']
            instagram = request.POST['instagram']
            facebook = request.POST['facebook']
            twitter = request.POST['twitter']
            member = Member(amci = amci, nom = fname, prenoms = lname, mail = mail, date_nais = date_nais, tel = tel, annee_bourse = annee_bourse, instagram = instagram, facebook = facebook, twitter = twitter)
            member.save()
            return redirect('admini:allMember')
    else:
        form = memberForm()
    return render(request, 'admini/newMember.html', {'form': form})



@login_required
def newPurchase(request):
    submitted = False
    if request.method == 'POST':
        form = treasuryForm(request.POST, request.FILES)
        if form.is_valid():
            nom = request.POST['nom']
            prix = request.POST['prix']
            date = request.POST['date']
            purchase = Treasury(nom = nom, prix = prix, date = date)
            purchase.save()
            return redirect('admini:allPurchase')
    else:
        form = treasuryForm()
    return render(request, 'admini/newPurchase.html', {'form': form})

@login_required
def allMember(request):
    members = Member.objects.all()
    paginator = Paginator(members, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admini/allMember.html', {'page_obj': page_obj})


@login_required
def allPurchase(request):
    purchase = Treasury.objects.all()
    paginator = Paginator(purchase, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admini/allPurchase.html', {'page_obj': page_obj})


@login_required
def deleteMember(request, member_id):
    member = Member.objects.get(id = member_id)
    member.delete()
    return redirect('admini:allMember')



@login_required
def editMember(request, member_id):
    if request.method == 'POST':
        instagram = request.POST['instagram']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        record = Member.objects.get(id = member_id)
        record.instagram = instagram
        record.facebook = facebook
        record.twitter = twitter
        record.save()
        return redirect('admini:allMember')

    else:
        members = Member.objects.get(id = member_id)
        return render(request, 'admini/editMember.html', {'members': members})




@login_required
def newMeeting(request):
    submitted = False
    if request.method == 'POST':
        form = meetingForm(request.POST, request.FILES)
        if form.is_valid():
            nom = request.POST['nom']
            pdf = request.FILES['pdf']
            meeting = Reunion(nom = nom, pdf = pdf)
            meeting.save()
            return redirect('admini:allMeeting')
    else:
        form = meetingForm()
    return render(request, 'admini/newMeeting.html', {'form': form})



@login_required
def allMeeting(request):
    meeting = Reunion.objects.all()
    paginator = Paginator(meeting, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admini/allMeeting.html', {'page_obj': page_obj})
