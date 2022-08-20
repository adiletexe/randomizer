from django.shortcuts import render
from random import choice, randint


# Create your views here.
def home(request):
    return render(request, 'randomizingsystem/home.html')

def randomized(request):
    # random order
    if request.GET.get('typeofrandomizing') == 'randomorder':
        splitted_text = list(map(str, (request.GET.get('text').split())))
        randomizedorder = []
        for i in range(len(splitted_text)):
            rand = choice(splitted_text)
            randomizedorder.append(rand)
            splitted_text.remove(rand)
        return render(request, 'randomizingsystem/randomized.html', {'randomizedorder': randomizedorder})
    # randomnumber
    elif request.GET.get('text1'):
        try:
            splitted_text = list(map(str, (request.GET.get('text1').split())))
            min = int(splitted_text[0])
            max = int(splitted_text[1])
            randomnumber = randint(min, max)
            return render(request, 'randomizingsystem/randomized.html', {'randomnumber': randomnumber})
        except:
            return render(request, 'randomizingsystem/randomnumber.html',
                          {'error': 'Aren\'t you lizard? Enter values correctly'})
    # 2 groups
    elif request.GET.get('typeofrandomizing') == '2':
        splitted_text = list(map(str, (request.GET.get('text').split())))
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
        splitted_text = list(map(str, (request.GET.get('text').split())))
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
        splitted_text = list(map(str, (request.GET.get('text').split())))
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
        splitted_text = list(map(str, (request.GET.get('text').split())))
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
        return render(request, 'randomizingsystem/randomnumber.html', {'error':'Aren\'t you lizard? Enter values correctly'})

def randomnumber(request):
    return render(request, 'randomizingsystem/randomnumber.html')

