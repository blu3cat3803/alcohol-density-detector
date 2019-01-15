from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from chart.models import alcohol

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"tests": 10})


def get_data(request, *args, **kwargs):
    data = {
        "tests": 10,
    }
    return JsonResponse(data) # http response



class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        time = []
        vol1 = []
        vol2 = []
        vol3 = []
        vol4 = []
        vol5 = []

        alc = list(alcohol.objects.all())
        length = len(alc)
        if length < 20:
            for x in range(length):
	        time.append(int(alc[x].t))
	        vol1.append(float(alc[x].v1))
                vol2.append(float(alc[x].v2))
                vol3.append(float(alc[x].v3))
                vol4.append(float(alc[x].v4))
                vol5.append(float(alc[x].v5))
        else:
            i = 21
            for x in range(20):
                time.append(int(alc[length - i].t))
                vol1.append(float(alc[length - i].v1))
                vol2.append(float(alc[length - i].v2))
                vol3.append(float(alc[length - i].v3))
                vol4.append(float(alc[length - i].v4))
                vol5.append(float(alc[length - i].v5))
                i = i - 1
        data = {
                "labels": time,
                "analog_v1": vol1,
                "analog_v2": vol2,
                "analog_v3": vol3,
                "analog_v4": vol4,
                "analog_v5": vol5,

        }
        return Response(data)

