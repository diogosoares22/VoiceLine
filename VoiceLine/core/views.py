# core > views.py

from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Record
import speech_recognition as sr
import subprocess
from backend.ml_model import *

def record(request):

    def convert(filename):
        new_filename = filename.split(".webm")[0] + ".wav"
        command = ['ffmpeg', '-i', filename, '-ac', '1', '-f', 'wav', new_filename]
        subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        return new_filename

    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        record = Record.objects.create(voice_record=audio_file)
        record.save()

        AUDIO_FILE = convert("media/" + str(record.voice_record))
        """
        # Using google API
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        """
        # Using facebook ml_model
        text = speech_to_audio(AUDIO_FILE)
        record.text = text
        record.save()

        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "success": True,
                "url": "http://127.0.0.1:8000/record/detail/" + str(record.id),
            }
        )
    context = {"page_title": "Record audio"}
    return render(request, "core/record.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "core/record_detail.html", context)


def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)

