run:
	venv/bin/python main.py

check:
	@echo "🔍 Запускаем статический анализ типов (mypy)..."
	venv/bin/mypy .
	@echo "🧹 Запускаем линтер (ruff)..."
	venv/bin/ruff check .
	@echo "✅ Все проверки пройдены!"