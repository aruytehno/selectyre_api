# selectyre_api
API для загрузки и подготовки данных для интернет магазина

### Описание алгоритма работы:
- [x] Скачать выгрузку с сервиса
- [x] Прочитать её
- [x] Записать в базу данных
---
- [ ] Выгрузить готовый - подготовленный .xlsx для визуального анализа с группировкой цен и количества
- [ ] Выгрузить готовый - подготовленный .csv для загрузки в интернет магазин
- [ ] Выгрузить готовый - подготовленный .yml для загрузки в яндекс - маркет

### Техническое задание

Задача:
Интегрировать сервис интернет-магазином на https://www.webasyst.ru/.
Задача:
- Настройка автоматической синхронизации 20 000 карточек товаров с выборкой из ~100 000 предоставляемых сервисом.
- Возможность загрузить из бота .csv файлы как по отдельности так и в формате единой таблицы для визуального анализа.
Особенности сервисов:
https://selectyre.ru/
- Предоставляет каталог товаров в форматах .csv, .json, .xml
- 5 ссылок выгрузки .csv: шины, остатки шин, диски, остатки дисков, склады на которых находятся единицы товара. 
- Данные находятся в отдельных таблицах и требуют совмещения в один список
https://www.webasyst.ru/
- Не позволяет производить обмен данными через API
- Куплен плагин для загрузки товаров из файла .xml который располагается на каком либо сервере.


---
Алгоритм решения данной задачи: 

Шаг 1: Настройка автоматической синхронизации

1.1 Получить доступ к API selectyre.ru для автоматической загрузки данных.

1.2 Создать скрипт для автоматической загрузки данных в форматах csv, json или xml в базу данных.

1.3 Настроить расписание для автоматической синхронизации данных с selectyre.ru, используя скрипт из пункта 1.2.

1.4 Создать таблицу в базе данных для хранения данных о товарах и их свойствах.

1.5 Использовать запросы SQL для загрузки данных из csv, json или xml файлов в таблицу базы данных.

1.6 Настроить механизм обновления данных для обновления информации о товарах в базе данных при синхронизации.

Шаг 2: Интеграция в телеграмм бот

2.1 Создать телеграмм бота.

2.2 Настроить бота для скачивания и загрузки данных о товарах из базы данных.

2.3 Добавить функцию обновления данных в бота, позволяющую обновлять информацию о товарах в базе данных.

2.4 Добавить функцию выгрузки данных в формате .yml для яндекс маркета в бота.

2.5 Добавить функцию загрузки данных в формате .csv для визуального анализа в бота.

2.6 Добавить функцию загрузки данных в формате единой таблицы для визуального анализа в бота.

2.7 Настроить механизм отправки данных из бота в базу данных для обновления информации о товарах.

Шаг 3: Интеграция с Google Merchant Center (не обязательный пункт)

3.1 Получить доступ к API Google Merchant Center для загрузки данных.

3.2 Создать скрипт для загрузки данных о товарах из базы данных в Google Merchant Center.

3.3 Настроить расписание для автоматической загрузки данных в Google Merchant Center, используя скрипт из пункта 3.2.

3.4 Настроить механизм обновления данных для обновления информации о товарах в Google Merchant Center при синхронизации.

### SQL

```text
-- Выборка по складам Москвы и Санкт-Петербурга
SELECT * FROM TIRE_ASSORTMENT, TIRE_REMNANTS
WHERE TIRE_ASSORTMENT.code = TIRE_REMNANTS.code
AND TIRE_REMNANTS.stock_name in ('brineks_moskva',
'yarshintorg_moskva',
'diskoptim_moskva',
'discovery_moskva',
'liga-tayres_moskva',
'shinservis_moskva',
'eksklyuziv_moskva',
'laserta_moskva',
'sever-avto_moskva-chernoe',
'sever-avto_moskva-elektrougli',
'sever-avto_moskva-pomorskaya',
'asia-tires_moskva',
'sever-avto-msk_moskva',
'kolesnyy-ryad_vidnoe',
'shinservis_pod-zakaz',
'avtorus_moskva',
'brineks_moskva-rrc-moskva',
'novyy-alyans_zakaz',
'fortochki_sklad-3-dlya-msk',
'fortochki_sklad-2-dlya-msk',
'fortochki_mosobl-yam-dlya-msk',
'fortochki_moskva-krs-dlya-msk',
'novyy-alyans_moskva',
'fortochki_sklad-4-dlya-msk',
'asia-tires_spb',
'1001-shina_spb',
'koleso-russia_spb',
'diskoptim_spb',
'poshk_spb',
'yarshintorg_sankt-peterburg',
'petrovskiy_spb',
'fortochki_sankt-peterburg-centr',
'fortochki_sankt-peterburg-2',
'paritet_spb',
'aksel_spb',
'fortochki_mosobl-yam',
'cooper_spb',
'shinservis_spb',
'avtoreal_sankt-peterburg',
'koleso-piter_spb',
'brineks_sankt-peterburg',
'tirealliance_spb',
'sever-avto-msk_sankt-peterburg',
'st-tuning_spb',
'eksklyuziv_sankt-peterburg',
'laserta_spb',
'rosshina_spb',
'alato_spb',
'hochu-shinu_spb',
'tyregroup_spb',
'petromaks_spb',
'tireshop_spb');
```


```sql
-- Усовершенствованый вариант выборки
SELECT 'product_variant' as 'Тип строки', MAX(TIRE_REMNANTS.price) as 'Цена', SUM(TIRE_REMNANTS.quantity) as 'В наличии', 1 as 'Доступен для заказа', 'НДС' as 'Облагается налогом', 'Шины' as 'Тип товаров', TIRE_ASSORTMENT.code as 'Код артикула',TIRE_ASSORTMENT.p_full_name as 'Наименование',
TIRE_ASSORTMENT.p_brand as 'Бренд',TIRE_ASSORTMENT.p_model as 'Модель', TIRE_ASSORTMENT.p_width as 'Ширина шины', TIRE_ASSORTMENT.p_height as 'Профиль',
TIRE_ASSORTMENT.p_diameter as 'Диаметр', TIRE_ASSORTMENT.p_load_index as 'Индекс нагрузки', TIRE_ASSORTMENT .p_speed_index as 'Индекс скорости', 
TIRE_ASSORTMENT.p_season as 'Сезон', TIRE_ASSORTMENT.p_category as 'Категория', TIRE_ASSORTMENT.p_runflat as 'Технология RunFlat', TIRE_ASSORTMENT .p_axis as 'Ось',
TIRE_ASSORTMENT .p_photo as 'Изображения товаров'  FROM TIRE_ASSORTMENT, TIRE_REMNANTS -- TIRE_REMNANTS.code, TIRE_REMNANTS.price, TIRE_REMNANTS.quantity
WHERE TIRE_ASSORTMENT.code = TIRE_REMNANTS.code
--AND TIRE_ASSORTMENT.code in ('t499602')
AND TIRE_REMNANTS.stock_name in ('brineks_moskva',
'yarshintorg_moskva',
'diskoptim_moskva',
'discovery_moskva',
'liga-tayres_moskva',
'shinservis_moskva',
'eksklyuziv_moskva',
'laserta_moskva',
'sever-avto_moskva-chernoe',
'sever-avto_moskva-elektrougli',
'sever-avto_moskva-pomorskaya',
'asia-tires_moskva',
'sever-avto-msk_moskva',
'kolesnyy-ryad_vidnoe',
'shinservis_pod-zakaz',
'avtorus_moskva',
'brineks_moskva-rrc-moskva',
'novyy-alyans_zakaz',
'fortochki_sklad-3-dlya-msk',
'fortochki_sklad-2-dlya-msk',
'fortochki_mosobl-yam-dlya-msk',
'fortochki_moskva-krs-dlya-msk',
'novyy-alyans_moskva',
'fortochki_sklad-4-dlya-msk',
'asia-tires_spb',
'1001-shina_spb',
'koleso-russia_spb',
'diskoptim_spb',
'poshk_spb',
'yarshintorg_sankt-peterburg',
'petrovskiy_spb',
'fortochki_sankt-peterburg-centr',
'fortochki_sankt-peterburg-2',
'paritet_spb',
'aksel_spb',
'fortochki_mosobl-yam',
'cooper_spb',
'shinservis_spb',
'avtoreal_sankt-peterburg',
'koleso-piter_spb',
'brineks_sankt-peterburg',
'tirealliance_spb',
'sever-avto-msk_sankt-peterburg',
'st-tuning_spb',
'eksklyuziv_sankt-peterburg',
'laserta_spb',
'rosshina_spb',
'alato_spb',
'hochu-shinu_spb',
'tyregroup_spb',
'petromaks_spb',
'tireshop_spb')
GROUP BY TIRE_REMNANTS.code;
```

```sql
-- Выгрузка для Север-Авто.
SELECT 'product_variant' as 'Тип строки', MAX(TIRE_REMNANTS.minimal_internet_price) as 'Цена', SUM(TIRE_REMNANTS.quantity) as 'В наличии', 1 as 'Доступен для заказа', 'НДС' as 'Облагается налогом', 'Шины' as 'Тип товаров', TIRE_ASSORTMENT.code as 'Код артикула',TIRE_ASSORTMENT.p_full_name as 'Наименование',
TIRE_ASSORTMENT.p_brand as 'Бренд',TIRE_ASSORTMENT.p_model as 'Модель', TIRE_ASSORTMENT.p_width as 'Ширина шины', TIRE_ASSORTMENT.p_height as 'Профиль',
TIRE_ASSORTMENT.p_diameter as 'Диаметр', TIRE_ASSORTMENT.p_load_index as 'Индекс нагрузки', TIRE_ASSORTMENT .p_speed_index as 'Индекс скорости', 
TIRE_ASSORTMENT.p_season as 'Сезон', TIRE_ASSORTMENT.p_category as 'Категория', TIRE_ASSORTMENT.p_runflat as 'Технология RunFlat', TIRE_ASSORTMENT .p_axis as 'Ось',
TIRE_ASSORTMENT .p_photo as 'Изображения товаров'  FROM TIRE_ASSORTMENT, TIRE_REMNANTS -- TIRE_REMNANTS.code, TIRE_REMNANTS.price, TIRE_REMNANTS.quantity
WHERE TIRE_ASSORTMENT.code = TIRE_REMNANTS.code
--AND TIRE_ASSORTMENT.code in ('t499602')
AND TIRE_REMNANTS.quantity > 20
AND TIRE_REMNANTS.stock_name in (
'sever-avto-msk_sankt-peterburg')
GROUP BY TIRE_REMNANTS.code;
```

```sql
-- Руссификация значений для RunFlat
UPDATE TIRE_ASSORTMENT 
SET p_runflat = REPLACE(p_runflat, 'True', 'Да')
WHERE p_runflat = 'True';

UPDATE TIRE_ASSORTMENT 
SET p_runflat = REPLACE(p_runflat, 'False', 'Нет')
WHERE p_runflat = 'False';
```

```sql
-- Подсчёт общего колличества строк в таблицах
SELECT COUNT(*)  FROM TIRE_ASSORTMENT;
SELECT COUNT(*) FROM TIRE_REMNANTS;
SELECT COUNT(*) FROM WHEELS_ASSORTMENT;
SELECT COUNT(*) FROM WHEELS_REMNANTS;
SELECT COUNT(*) FROM WAREHOUSE_ADDRESSES;
```
