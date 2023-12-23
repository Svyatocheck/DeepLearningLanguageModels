# Телеграм-бот для поиска релевантных резюме и вакансий
![Alt Text](assets/demonstration_gif.gif)


<div align="center">
    
  <a href="https://github.com/Svyatocheck/DeepLearningPractice/issues">![GitHub issues](https://img.shields.io/github/issues/Svyatocheck/DeepLearningPractice/issues)</a>
  <a href="https://github.com/Svyatocheck/DeepLearningPractice/blob/master/LICENSE">![GitHub license](https://img.shields.io/github/license/Svyatocheck/DeepLearningPractice?color=purple)</a>
  <a href="https://github.com/psf/black">![Code style](https://img.shields.io/badge/code%20style-black-black)</a>
    
</div>

### Stack: 

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)



### Репозиторий:

- assets - графические материалы для Readme файлика
- data_experiments - ноутбуки с обработкой датасетов
- model_experiments - ноутбуки с обучением моделек
- model_weights - лучшие веса обученных моделек

## Контент
- [Детекция дорожных знаков](#)
  - [Контент](#контент)
  - [Проблема](#проблема)
  - [Описание](#описание)
  - [Детекция знаков](#детекция-знаков)
    - [Данные](#данные)
    - [Статьи](#статьи)
    - [Архитектура](#архитектура)
    - [Демо](#демонстрация)
  - [Future Roadmap](#future-roadmap)
  - [Сравнение моделей](#сравнение-моделей)
  - [Contribution](#contributing)
  - [Вывод](#conclusion)
  - [Авторы](#authors)

## Проблема
Данный продукт решает следующие проблемы:
* Автоматическая выдача нужного резюме или вакансии
* Удобный юзер интерфейс
* Быстрый инференс

## Описание
Предлагаемый телеграм-бот предоставляет пользователю возможность найти релевантную вакансию или резюме по своему запросу. 

Все собранные данные хранятся в централизованной базе данных для последующего анализа и обучения модели.

## Структура проекта
### Данные
[Данные](https://drive.google.com/file/d/1ikA_Ht45fXD2w5dWZ9sGTSRl-UNeCVub/view)


### Frontend
![Alt text](assets/mvp_preview.png)

### Архитектура


### Особенности и ограничения 
- 

## Future  Roadmap
- Проверить дополнительные архитектуры для преобразования текста в векторный формат(T5, DeepPavlov BERT)
- Улучшить инференс
- Обучить модель на бОльшем наборе данных
- Улучшить взаимодействие с пользователем

## Сравнение моделей

Между собой сравнивались две модели для преобразования текста в векторный формат - модель E5 и модель ruBERT. 
В итоге была выбрана модель **E5**, потому что она отрабатывала лучше в сравнении с моделью ruBERT.

## Contributing
Скопируйте файл [`contributing.md`](https://github.com/Svyatocheck/DeepLearningPractice/blob/master/contributing.md).

## Вывод
Предлагаемый телеграм-бот представляет комплексное решение проблемы поиска нужных вакансий и резюме.

Благодаря алгоритмам нейронных сетей, эффективному управлению данными и быстроте функционирования, он представляет собой надежный 
инструмент и может использоваться на реальных кейсах.

## Авторы
- [Vladimir Dimitrov](https://github.com/Vladimir-Dimitrov-Ngu)
- [Vladimir Kravtsov](https://github.com/VladimirKravtsov36)
- [Dmitrii Klimenchenko](https://github.com/dimages)
- [Svyatoslav Ivanov](https://github.com/Svyatocheck)
