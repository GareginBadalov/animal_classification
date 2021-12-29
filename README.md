# animal_classification python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/agajorte/zoo-animals-extended-dataset

Задача: предсказать по описанию животного его класс (поле fraudulent). Мультиклассовая классификация

Используемые признаки:

- hair (text)
- feathers (text)
- eggs (text)
- milk (text)
- airborne (text)
- aquatic (text)
- predator (text)
- toothed (text)
- backbone (text)
- breathes (text)
- venomous (text)
- fins (text)
- legs (text)
- tail (text)
- domestic (text)
- catsize (text)

Модель: logreg

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/GareginBadalov/animal_classification
$ cd animal_classification
$ docker build -t animal_classification .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -v C:\projects\animal_classification:/animal_classification/animal_classification/models animal_classification
```
### Переходим на http://localhost:8180
### Отправляем POST на http://localhost:8180/predict

#JSON для отправки запроса
{

	"hair": 0,
	"feathers": 0,
	"eggs": 1,
	"milk": 0,
	"airborne": 0,
	"aquatic": 1,
	"predator": 0,
	"toothed": 0,
	"backbone": 1,
	"breathes": 1,
	"venomous": 0,
	"fins": 0,
	"legs": 4,
	"tail": 1,
	"domestic": 1,
	"catsize": 1
}