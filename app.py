from flask import Flask #создаем объект класса фласк

app = Flask(__name__)
@app.route("/") #создание маршрута
def hello_world(): #функция, которая будет вызвана при запросе к маршруту
  return "Hello world!" #возвращаем строку

if __name__ == "__main__": #проверка на запуск самого скрипта 
  app.run(host="0.0.0.0", debug=True) #запуск приложения