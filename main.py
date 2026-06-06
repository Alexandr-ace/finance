from dataclasses import dataclass
# venv\Scripts\activate.bat для виндовс
# source venv/bin/activate для мака
# pip install -r requirements.txt
# Начни с базового скрипта
import requests
from bs4 import BeautifulSoup


# 1. Сделай запрос к WB API или спарси страницу
# 2. Сохрани данные в SQLite (проще всего для начала)

# 1. Это аналог struct в Rust. Мы жестко задаем типы полей.
# @dataclass
