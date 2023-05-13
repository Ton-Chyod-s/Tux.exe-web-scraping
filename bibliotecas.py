# Bibliotecas para trabalhar com Selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (frame_to_be_available_and_switch_to_it, element_to_be_clickable)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Edge, Chrome, Ie, Firefox
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.ie.service import Service as IEService
#from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# Bibliotecas para trabalhar com arquivos e diretórios
from openpyxl import load_workbook
from lxml import etree
import shutil
import zipfile
import csv
# Bibliotecas para trabalhar com interface gráfica
import PySimpleGUI as sg
# Bibliotecas para trabalhar com data e hora
from time import sleep
import time
# Bibliotecas para trabalhar com rede e internet
import requests
import socket
import googlemaps
# Outras bibliotecas
from pynput import mouse
from random import randint
from unidecode import unidecode 
from tqdm import tqdm
import pyautogui as pt
import random
import os
import pandas as pd
import xml.etree.ElementTree as et
import keyboard
import sys
import json
