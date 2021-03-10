distance = int(input('Digite uma distância em metros: '))

km = distance/1000
hm = distance/100
dam = distance/10
cm = distance*100
mm = distance*10000

print('{}km, {}hm, {}dam, {}m, {}cm, {}mm'.format(km, hm, dam, distance, cm, mm))
