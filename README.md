# DeepLearningLanguageModels
Simple telegram bot to demonstrate language model.


# Детекция дорожных знаков на видеорегистраторе

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
    - [Видео](#видео)
    - [Архитектура](#архитектура)
    - [Демо](#демонстрация)
      - [Особенности и ограничения](#особенности-и-ограничения-системы)
  - [Future Roadmap](#future-roadmap)
  - [Сравнение моделей](#сравнение-моделей)
  - [Contibution](#contributing)
  - [Вывод](#conclusion)
  - [Авторы](#authors)

## Проблема
Данный продукт решает следующие проблемы:
* Автоматическая выдача нужного резюме или вакансии
* Удобный юзер интерфейс
* Быстрый инференс

## Описание
Предлагаемая система видеонаблюдения предназначена для обеспечения комплексного мониторинга и обнаружения дорожных знаков. 

Все собранные данные хранятся в централизованной базе данных для последующего анализа и обучения модели.

## Детекция знаков
### Данные
[Данные](https://drive.google.com/file/d/1ikA_Ht45fXD2w5dWZ9sGTSRl-UNeCVub/view)

### Видео
[Про разметку](https://www.youtube.com/watch?v=wjgnYyU6Ymc)

### Архитектура

<p align="center" width="100%">
    <img width="80%" src="assets/architecture.png">
</p>

### Frontend
![Alt text](assets/mvp_preview.png)

#### Особенности и ограничения 
- В текущей версии приложения ограничение по размеру видео составляет 200 МБ. Это важно учитывать при загрузке видеоматериалов.
- **Загрузка файлов**: пользователи могут загружать видеофайлы в форматах, таких как mp4, mov, avi, asf, m4v и mpeg-4. Загрузка происходит способом drag and drop. Во время загрузки пользователь видит сообщение «Upload a video». После успешной загрузки пользователь видит сообщение «Upload successful!».
- **Обработка видео**: приложение обрабатывает видео с использованием CV-модели. После завершения обработки пользователь видит соответствующий индикатор: «Extracting complete!».
- **Video**: после обработки отображается загруженное видео с ограничивающей рамкой (bounding box) в месте, где модель детектировала дорожный знак.

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
