## GeometryLib
---
GeometryLib - это библиотека Python для вычисления площади различных геометрических фигур.
***
## Содержание
<details>
 <summary> Инструкции по установке и запуску </summary>
  
**Клонирование репозитория**
```bash
git clone git@github.com:VlKazmin/test_geometrylib
```

**Локальная Установка библиотеки**:
```bash
pip install .
```
</details>

<details>
 <summary> Запуск примеров </summary>
 
```bash
python example.py
```
 </details>
 
 <details>
 <summary> Запуск тестов </summary>
 
```bash
python -m unittest discover -s tests
```
 </details>
 <details>
 <summary> Условия задания </summary>
 <br>
   Напишите на Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:
 </br>

- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным

  </details>
