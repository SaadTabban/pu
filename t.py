
import pytz
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from pydub import AudioSegment
from pydub.silence import split_on_silence

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, constants
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, Updater, Filters, MessageHandler
import logging
import telegram

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display


from pdf2image import convert_from_path

from PIL import Image, ImageDraw, ImageFont

import pytesseract
import secrets

import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
