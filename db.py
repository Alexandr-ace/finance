import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

# 1. Загружаем переменные из файла .env
load_dotenv()

def get_db_connection():
    try:
        # 2. Подключаемся к базе данных
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("✅ Успешное подключение к PostgreSQL!")
        return connection
    except Error as e:
        print(f"❌ Ошибка при подключении к PostgreSQL: {e}")
        return None

def setup_database():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # 3. Создаем таблицу для товаров WB (если её еще нет)
            create_table_query = """
            CREATE TABLE IF NOT EXISTS wb_products (
                id SERIAL PRIMARY KEY,
                article VARCHAR(50) UNIQUE NOT NULL,
                name VARCHAR(255) NOT NULL,
                price INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("✅ Таблица wb_products успешно создана или уже существует.")
            
            # 4. Тестовая вставка данных (имитация работы парсера)
            insert_query = """
            INSERT INTO wb_products (article, name, price) 
            VALUES (%s, %s, %s)
            ON CONFLICT (article) DO NOTHING;
            """
            # Данные для теста
            test_data = ("12345678", "Тестовая футболка", 1500)
            cursor.execute(insert_query, test_data)
            connection.commit()
            print("✅ Тестовые данные успешно добавлены!")
            
        except Error as e:
            print(f"❌ Ошибка при работе с БД: {e}")
        finally:
            # 5. Обязательно закрываем соединение
            if connection:
                cursor.close()
                connection.close()
                print("🔌 Соединение с PostgreSQL закрыто.")

if __name__ == "__main__":
    setup_database()