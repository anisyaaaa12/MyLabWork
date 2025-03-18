import psycopg2

# Подключаемся к базе данных
conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)

# Создаём курсор для выполнения запросов
cur = conn.cursor()

# Выполнение запроса
cur.execute("SELECT * FROM your_table")

# Получаем результаты
rows = cur.fetchall()
for row in rows:
    print(row)

# Закрываем соединение
cur.close()
conn.close() 
