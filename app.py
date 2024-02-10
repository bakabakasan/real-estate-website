from flask import Flask, render_template #создаем объект класса фласк, добавляем методы для работы с html

app = Flask(__name__)
@app.route("/") #создание маршрута
def hello_world(): #функция, которая будет вызвана при запросе к маршруту
  return render_template('home.html') #возвращаем файл html

if __name__ == "__main__": #проверка на запуск самого скрипта 
  app.run(host="0.0.0.0", debug=True) #запуск приложения