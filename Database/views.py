# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json as simplejson
import sys

from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms.models import model_to_dict

from forms import testForm, entryForm

from .models import Entry, Dictionary


# Create your views here.

def index(request):
    return render(request, 'Database/index.html')

def entry_list2(request):
    file = request.FILES['myfile'] # this is my file
    contentOfFile = file.read()
    form = entryForm()
    entries = []

    try:
        print >> sys.stderr, "FILE: ", contentOfFile
        data = simplejson.loads(contentOfFile)
    except ValueError:
        # messages.error(request, "Something wrong with JSON format")
        messages.warning(request, 'Wrong JSON format.')
        # return JsonResponse({'status': 'false', 'message': "didnt parse a correct JSON file"}, status=500)
        # return render(request, 'Database/index.html')
        return HttpResponseRedirect('/Database/')
    else:
        # contentOfFile.encode('utf-8')
        print >> sys.stderr, "data: ", data
        #d = Dictionary.objects.create(language="test")
        #d.save()

        for item in data:
            print >> sys.stderr, "item: ", item
#            print >> sys.stderr, item['word']
            e = Entry.objects.create(dictionary=d)

            for key in item:
                print >> sys.stderr, key, ": ", item[key]
                if (key == 'database'):
                    d = Entry.objects.get_or_create(pk=item[key])
                    e.__setattr__(key,d)
                else:
                    e.__setattr__(key,item[key])

            e.save()

            print >> sys.stderr, e.word
            e.refresh_from_db()
            print >> sys.stderr, e.get_entry()
            entries = Entry.objects.filter(dictionary__language='test')

        return render(request, 'Database/entry_list.html', {'file': file, 'entries': entries, 'form': form, 'id': d.pk})

def entry_list(request):
    file = request.FILES['myfile'] # this is my file
    contentOfFile = file.read()
    form = entryForm()
    entries = []
    created = 0
    created_total = 0

    try:
        print >> sys.stderr, "FILE: ", contentOfFile
        data = simplejson.loads(contentOfFile)
    except ValueError:
        # messages.error(request, "Something wrong with JSON format")
        messages.warning(request, 'Wrong JSON format.')
        # return JsonResponse({'status': 'false', 'message': "didnt parse a correct JSON file"}, status=500)
        # return render(request, 'Database/index.html')
        return HttpResponseRedirect('/Database/')
    else:
        # contentOfFile.encode('utf-8')
        print >> sys.stderr, "data: ", data
        #d = Dictionary.objects.create(language="test")
        #d.save()

        print >> sys.stderr, "first item: ", data[0]
        print >> sys.stderr, "first dictionary: ", data[0]['dictionary']
        (d,created) = Dictionary.objects.get_or_create(id = data[0]['dictionary'])
        print >> sys.stderr, "dictionary name: ", d.language
        print >> sys.stderr, "Needed to create a new dictionary?: ", created

        for item in data:
            print >> sys.stderr, "item: ", item
            print >> sys.stderr, "item.id: ", item['id']
            (e,created) = Entry.objects.get_or_create(id = item['id'],dictionary=d)
            e.__setattr__('word',item['word'])
            e.__setattr__('gr',item['gr'])
            e.__setattr__('ph',item['ph'])
            e.__setattr__('CVC',item['CVC'])
            e.save()
            print >> sys.stderr, "created: ", created
            created_total += created

        print >> sys.stderr, "new entries created: ", created_total
        entries = Entry.objects.filter(dictionary=d.pk)
        print >> sys.stderr, "Entries: ", entries
        return render(request, 'Database/entry_list.html', {'file': file, 'entries': entries, 'form': form, 'd':d,'id': d.pk})


def post_list(request):
    d = Dictionary.objects.all().first()
    entries = Entry.objects.filter(dictionary=d)
   # e = entries.first()
   # d = Dictionary.objects.get(pk=e.dictionary.pk)
    return render(request, 'Database/post_list.html', {'entries': entries, 'd': d, 'id': d.pk})

def entry(request):
    data = {"word": "John","CVC": "CVC","gr": "J oh n","ph": "j O n"}
    return render(request, 'Database/readit.html', {'file': file, 'data': data})
#    form = entryForm(request.POST or None, initial={'data': data})
#    if form.is_valid():
        # validate and save
#        pass

#    template = 'entry.html'
#    context = RequestContext(request, {'form': form})
#    return render_to_response(template, context)


def entry_new(request, pk):
    if request.method == "POST":
        form = entryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.dictionary = Dictionary.objects.get(id=pk)
            entry.save()
            print >> sys.stderr, "saved word: ", entry.word
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = entryForm()

    return render(request, 'Database/entry_edit.html', {'form': form})





#cat unformatted.json | python -m json.tool > formatted.json
#simplejson.dump(jin,fout)
# fout.close()




def entry_detail(request, pk):
    form = entryForm()
    entry = Entry.objects.get(id=pk)
    return render(request, 'Database/entry_detail.html', {'form': form, 'entry': entry})


def readit(request):
    return None

def write(request):
    d = Dictionary.objects.all().first()
  #  print >> sys.stderr, d
    entries = Entry.objects.filter(dictionary=d)
  #  print >> sys.stderr, entries[0].pk
    jsonarray = []
    for e in entries:
        m = model_to_dict(e)
        #print >> sys.stderr, m
        jsonarray.append(m)

    #print >> sys.stderr, jsonarray, len(simplejson.dumps(jsonarray))

    response = HttpResponse(simplejson.dumps(jsonarray).decode('string_escape'), content_type='application/w')
    response['Content-Length'] = len(simplejson.dumps(jsonarray).decode('string_escape'))
    response['Content-Disposition'] = 'attachment; filename = dictionary.json'

    #print >> sys.stderr, response
    return response

def write2(request):
    d = Dictionary.objects.filter(language='test')
    print >> sys.stderr, d
    entries = Entry.objects.filter(dictionary=d[0])
    print >> sys.stderr, entries[0].pk
    jsonarray = []
    for e in entries:
        m = model_to_dict(e)
        print >> sys.stderr, m
        jsonarray.append(simplejson.dumps(m))
        print >> sys.stderr, jsonarray
    return render(request,'Database/write.html',{'jsonarray': jsonarray})


def entry_edit(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = entryForm(request.POST, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = entryForm(instance=post)
    return render(request, 'Database/entry_edit.html', {'form': form})