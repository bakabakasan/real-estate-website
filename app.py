from flask import Flask, render_template, jsonify #создаем объект класса фласк, добавляем методы для работы с html, функцию для работы с списком данных

app = Flask(__name__)

ESTATE = [
  {
    'id': 1, 
    'type': 'Квартира',
    'location': 'Минск, Беларусь',
    'cost': '90 000$',
    'rooms': '2',
  },
  {
    'id': 2, 
    'type': 'Квартира',
    'location': 'Гродно, Беларусь',
    'cost': '30 000$',
    'rooms': '1',
  },
  {
    'id': 3, 
    'type': 'Дом',
    'location': 'Витебск, Беларусь',
    'cost': '',
    'rooms': '3',
  },
  {
    'id': 4, 
    'type': 'Дом',
    'location': 'Полоцк, Беларусь',
    'cost': '100 000$',
    'rooms': '4',
  } #создаём список объектов
]
@app.route("/") #создание маршрута
def hello_dreamhouse(): #функция, которая будет вызвана при запросе к маршруту
  return render_template('home.html', 
                         estates=ESTATE) 
  #возвращаем файл html, добавляем аргумент estate

@app.route("/api/estates")
def list_estates():
  return jsonify(ESTATE) #создаём новую функцию и решестрируем в маршруте

if __name__ == "__main__": #проверка на запуск самого скрипта 
  app.run(host="0.0.0.0", debug=True) #запуск приложения