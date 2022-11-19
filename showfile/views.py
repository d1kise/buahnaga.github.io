from django.shortcuts import render
import json, csv
import xml.etree.ElementTree as ET

#home/index.html
def showfile(request):

    context={
        'page_title':'Home',
    }

    return render(request, 'home/index.html',context)

#csv/csv.html
def lihatcsv(request):
    reader = csv.DictReader(open("static/Cars.csv"))
    print(reader)
    csvview=[]

    class CostumArrayCSV:    
        def __init__(self, idcsv, nama, harga):
            self.idcsv = idcsv
            self.nama = nama
            self.harga = harga
    for row in reader:
        csvview.append(CostumArrayCSV(row['Id'], row['Name'], row['Price']))
     
    context={
        'page_title':'Preview CSV',
        'lihatCSV':csvview,
    }

    return render(request, 'csv/csv.html',context)

#json/json.html
def lihatjson(request):
    data = open('static/Cars.json').read()
    datjson = json.loads(data)
    jsondict = {}
    jsonview = []

    class CostumArrayJson:    
        def __init__(self, idJson, nama, harga):
            self.idJson = idJson
            self.nama = nama
            self.harga = harga

    for index, value in enumerate(datjson):
        jsondict[index] = value
    for i in jsondict:
        jsonview.append(CostumArrayJson(jsondict[i]['Id'], jsondict[i]['Name'], jsondict[i]['Price']))

    context={
        'page_title':'Preview Json',
        'lihatJson' : jsonview,
    }

    return render(request, 'json/json.html',context)

#xml/xml.html
def lihatxml(request):
    myroot = ET.parse('static/Cars.xml')
    root = myroot.getroot()
    xmlview = []

    class CostumArrayXML:    
        def __init__(self, idxml, nama, harga):
            self.idxml = idxml
            self.nama = nama
            self.harga = harga
    for x in root.findall('row'):
        if x.find('Id').text != 'Id':
            xmlview.append(CostumArrayXML(x.find('Id').text,  x.find('Name').text, x.find('Price').text))

    context={
        'page_title':'Preview XML',
        'lihatXML' : xmlview,
    }

    return render(request, 'xml/xml.html', context)