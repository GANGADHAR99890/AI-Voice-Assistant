import datetime
import os
import signal
import speech_recognition as sr
import pyttsx3
import webbrowser
import re
import pywhatkit
import pyjokes
import requests
import json
import cv2
r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 200)