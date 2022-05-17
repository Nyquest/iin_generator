# Генерация тестовых и валидных ИИНов

ИИН - Индивидуальный идентификационный код физического лица в Республике Казахстан

Готовый сгенерированный набор из 20 миллионов ИИНов можно скачать архивом (https://drive.google.com/file/d/1SIfp_CRl4cQetc3Kw2jqDcWpF3fYPc2s/view?usp=sharing)

Генерация происходит в соответствии с половозрастными характеристиками населения Республики Казахстан, так как эти данные кодируются в ИИНы.

Информация взята с сайта https://population.un.org/wpp/Download/Standard/Population/

Необходимо запустить скрипт iin_generator.py.

Входные данные берутся из файла qaz_population_2020.txt.
За основу взяты данные 2020 года.

Сгенерированные ИИНы записываются в выходной файл iin.txt.

Примечание
1) У сгенеренных ИИН первые 6 цифр ИИНа соответствуют действительной дате, хотя в настоящих ИИНах это правило нарушается;
2) У сгенеренных ИИН правильный контрольный разряд, хотя в настоящих ИИНах встречается некорретные контрольные разряды;
3) У сгенеренных ИИН правильный контрольный разряд, исключены ИИНы с контрольной суммой равной 10, т.к. контрольный разряд должен быть от 0 до 9. 

|   Age |    Both |    Male | Femail |
| ----- | ------- | ------- | ------ |
|   0-4 | 1920000 |  990000 | 930000 |
|   5-9 | 1948000 | 1001000 | 947000 |
| 10-14 | 1604000 |  825000 | 779000 |
| 15-19 | 1117000 |  572000 | 545000 |
| 20-24 | 1100000 |  564000 | 536000 |
| 25-29 | 1473000 |  740000 | 733000 |
| 30-34 | 1658000 |  815000 | 843000 |
| 35-39 | 1336000 |  666000 | 670000 |
| 40-44 | 1184000 |  581000 | 603000 |
| 45-49 | 1103000 |  534000 | 569000 |
| 50-54 |  978000 |  459000 | 519000 |
| 55-59 | 1062000 |  485000 | 576000 |
| 60-64 |  811000 |  353000 | 458000 |
| 65-69 |  628000 |  248000 | 380000 |
| 70-74 |  320000 |  119000 | 201000 |
| 75-79 |  233000 |   74000 | 159000 |
| 80-84 |  216000 |   64000 | 152000 |
| 85-89 |   62000 |   17000 |  45000 |
| 90-94 |   23000 |    5000 |  18000 |
| 95-99 |    3000 |       0 |   3000 |
|  100+ |       0 |       0 |      0 |