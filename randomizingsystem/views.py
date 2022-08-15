from django.shortcuts import render
from random import choice

# Create your views here.
def home(request):
    return render(request, 'randomizingsystem/home.html')

def randomized(request):
    splitted_text = list(map(str, (request.GET.get('text').split())))
    # random order
    if request.GET.get('typeofrandomizing') == 'randomorder':
        randomizedorder = []
        for i in range(len(splitted_text)):
            rand = choice(splitted_text)
            randomizedorder.append(rand)
            splitted_text.remove(rand)
        return render(request, 'randomizingsystem/randomized.html', {'randomizedorder': randomizedorder})
    # 2 groups
    elif request.GET.get('typeofrandomizing') == '2':
        team1 = []
        team2 = []
        for i in range(len(splitted_text)):
            try:
                #team1
                rand = choice(splitted_text)
                team1.append(rand)
                splitted_text.remove(rand)
                # team2
                rand2 = choice(splitted_text)
                team2.append(rand2)
                splitted_text.remove(rand2)
            except:
                break
        randomized = [team1, team2]
        return render(request, 'randomizingsystem/randomized.html', {'randomized': randomized})
    # 3 groups
    elif request.GET.get('typeofrandomizing') == '3':
        team1 = []
        team2 = []
        team3 = []
        for i in range(len(splitted_text)):
            try:
                #team1
                rand = choice(splitted_text)
                team1.append(rand)
                splitted_text.remove(rand)
                # team2
                rand2 = choice(splitted_text)
                team2.append(rand2)
                splitted_text.remove(rand2)
                # team3
                rand3 = choice(splitted_text)
                team3.append(rand3)
                splitted_text.remove(rand3)
            except:
                break
        randomized = [team1, team2, team3]
        return render(request, 'randomizingsystem/randomized.html', {'randomized': randomized})
    elif request.GET.get('typeofrandomizing') == '4':
        team1 = []
        team2 = []
        team3 = []
        team4 = []
        for i in range(len(splitted_text)):
            try:
                #team1
                rand = choice(splitted_text)
                team1.append(rand)
                splitted_text.remove(rand)
                # team2
                rand2 = choice(splitted_text)
                team2.append(rand2)
                splitted_text.remove(rand2)
                # team3
                rand3 = choice(splitted_text)
                team3.append(rand3)
                splitted_text.remove(rand3)
                # team4
                rand4 = choice(splitted_text)
                team4.append(rand4)
                splitted_text.remove(rand4)
            except:
                break
        randomized = [team1, team2, team3, team4]
        return render(request, 'randomizingsystem/randomized.html', {'randomized': randomized})
    elif request.GET.get('typeofrandomizing') == '6':
        team1 = []
        team2 = []
        team3 = []
        team4 = []
        team5 = []
        team6 = []
        for i in range(len(splitted_text)):
            try:
                #team1
                rand = choice(splitted_text)
                team1.append(rand)
                splitted_text.remove(rand)
                # team2
                rand2 = choice(splitted_text)
                team2.append(rand2)
                splitted_text.remove(rand2)
                # team3
                rand3 = choice(splitted_text)
                team3.append(rand3)
                splitted_text.remove(rand3)
                # team4
                rand4 = choice(splitted_text)
                team4.append(rand4)
                splitted_text.remove(rand4)
                # team5
                rand5 = choice(splitted_text)
                team5.append(rand5)
                splitted_text.remove(rand5)
                # team6
                rand6 = choice(splitted_text)
                team6.append(rand6)
                splitted_text.remove(rand6)
            except:
                break
        randomized = [team1, team2, team3, team4, team5, team6]
        return render(request, 'randomizingsystem/randomized.html', {'randomized': randomized})
    else:
        return render(request, 'randomizingsystem/home.html', {'error':'Something gone wrong!'})