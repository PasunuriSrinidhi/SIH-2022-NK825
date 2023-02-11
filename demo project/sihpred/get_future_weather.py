import pickle
import numpy as np
import json
import requests
import pandas as pd

import math
longi_m = pickle.load(open('m1.pkl', 'rb'))
lati_m = pickle.load(open('m2.pkl', 'rb'))
def get_data_api(longi,lati):
    Ilong = str(longi)
    Ilat = str(lati)
    api_url = "https://api.worldweatheronline.com/premium/v1/marine.ashx?key=2bbc79b15b214ec99fe104321231102&format=json&q=" + Ilong + "," + Ilat
    data = requests.get(api_url).json()
    tr = {'0': '00:00:00', '300': '03:00:00', '600': '06:00:00', '900': '09:00:00', '1200': '12:00:00',
          '1500': '15:00:00', '1800': '18:00:00', '2100': '21:00:00'}
    l = []

    for i in data['data']['weather']:

        for j in i['hourly']:
            furd = i['date']  # future date
            furt = tr[j['time']]  # future time

            furws = 0.277778 * (float(j['windspeedKmph']))  # futrewindSpeedmagnitude
            furwsh = furws * math.cos(math.radians(float(j['winddirDegree'])))  # horizontal component
            furwsv = furws * math.sin(math.radians(float(j['winddirDegree'])))  # vertical componet
            furp = float(j['pressure'])  # futurepressure hpa
            fursst = float(j['waterTemp_C'])  # sea surface temperature celsius
            e = [furd + " " + furt, fursst, furp, furwsh, furwsv, ]
            l.append(e)
    return l

#rest input search
#lastat input last known time
def get_coor(longi,lati,lastat):
    Ilong=str(longi)
    Ilat=str(lati)
    api_url = "https://api.worldweatheronline.com/premium/v1/marine.ashx?key=2bbc79b15b214ec99fe104321231102&format=json&q=" + Ilong + "," + Ilat
    data = requests.get(api_url).json()
    tr = {'0': '00:00:00', '300': '03:00:00', '600': '06:00:00', '900': '09:00:00', '1200': '12:00:00',
          '1500': '15:00:00', '1800': '18:00:00', '2100': '21:00:00'}
    l = []

    for i in data['data']['weather']:

        for j in i['hourly']:
            furd = i['date']  # future date
            furt = tr[j['time']]  # future time

            furws = 0.277778 * (float(j['windspeedKmph']))  # futrewindSpeedmagnitude
            furwsh = furws * math.cos(math.radians(float(j['winddirDegree'])))  # horizontal component
            furwsv = furws * math.sin(math.radians(float(j['winddirDegree'])))  # vertical componet
            furp = float(j['pressure'])  # futurepressure hpa
            fursst = float(j['waterTemp_C'])  # sea surface temperature celsius
            e = [furd + " " + furt, fursst, furp, furwsh, furwsv, ]
            l.append(e)



    yb=0
    for i in range(len(l)):
        t=l[i][0]
        m=t.split()
        ti=m[-1]#time
        er=ti.split(":")#list hors mints secs current api
        mk=lastat.split(":")
        j=er
        if int(j[0])>int(mk[0]):
            break

        if int(j[0])==int(mk[0]):
            if int(j[1])>int(mk[1]):
                break
        if int(j[0])==int(mk[0]):
            if int(j[1]) == int(mk[1]):
                if int(j[2])>int(mk[2]):
                    break
        if int(j[0])==int(mk[0]):
            if int(j[1]) == int(mk[1]):
                if int(j[2])==int(mk[2]):
                    break
        yb+=1
    l=l[yb:]
    d={}
    print(l)
    change_x=0
    change_y=0
    current_x=lati
    current_y=longi
    ymir=[]

    cusst=l[0][1]#current sst
    cuatms=l[0][2]#current atms
    cuhs=l[0][3]#current horizontal speed
    cuvs=l[0][4]#current vertical speed
    mui=[cusst,cuatms,cuhs,cuvs]

    changelongi=longi_m.predict([mui])
    changelati=lati_m.predict([mui])
    ymir.append([changelati[0],changelongi[0]])

    current_y+=round(changelongi[0],5)
    current_x+=round(changelati[0],5)
    d[l[0][0]]=[current_y,current_x]
    mui=[]

    while(yb<len(l)):
        print(l[yb][0])
        hui=get_data_api(current_y,current_x)
        rendu=[]

        for i in hui:

            if i[0]==l[yb][0]:
                rendu=[i[1],i[2],i[3],i[4]]
        mui=rendu




        mui=[l[yb][1],l[yb][2],l[yb][3],l[yb][4]]

        changelongi=longi_m.predict([mui])
        changelati=lati_m.predict([mui])
        current_y += round(changelongi[0], 5)
        current_x += round(changelati[0], 5)
        d[l[yb][0]]=[current_y,current_x]

        yb+=1





        # rhino=0
        # hij=resta.split(":")
        # for j in er:
        #     if int(j[0]) < int(mk[0]):
        #         break
        #
        #     if int(j[0]) == int(mk[0]):
        #         if int(j[1]) < int(mk[1]):
        #             break
        #
        #     rhino += 1
        #
        # if rhino<=yb:
        #     return "false data"
        #
        # mk=mk[yb:rhino]
    return d

print(get_coor(45,-2,'12:00:00'))