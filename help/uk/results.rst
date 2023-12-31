﻿Результати
===========

Коли dupeGuru завершення сканування на наявність дублікатів, він покаже його результати у вигляді дубліката список групи.

Про дублікат групи
----------------------

Дублікат група являє собою групу файлів, які весь матч разом. Кожна група має **посиланням**  на файл і одного або більше **однакових файлів**. Посилання файл перший файл групи. Його марка вікно вимкнено. Під ним, і з відступом, які дублікатів файлів.

Ви можете відзначити дублікатів файлів, але ви ніколи не можете помітити посилання файл групи. Це захід безпеки, щоб запобігти dupeGuru від видалення не тільки повторювані файли, але їх посилання. Ти впевнений, що не хочу цього, чи не так?

Що визначає, які файли посилання і які файли є дублікатами спочатку свою папку держави. Файл з посиланням папка завжди буде посилання в дублікат групи. Якщо всі файли зі звичайної папки, розмір визначити, який файл буде ведення дублікат групи. dupeGuru припускає, що ви завжди хочете зберегти найбільших файл, так що великих файлів займе вихідне положення.

Ви можете змінити посилання файл групи вручну. Для цього виберіть дублікат файлу, який ви хочете просувати на посилання, і натисніть на кнопку **Дії -> Додати вибраної посилання**.

Перегляд результатів
--------------------

Хоча ви можете просто натиснути на **Правка -> Виділити все, а потім** **Дії -> Отправить Позначено до кошику** швидко видалити всі дублікати файлів в результатах, завжди рекомендується переглянути всі дублікати перед видаляючи їх.

Щоб допомогти вам огляд результатів, ви можете викликати панель **Докладніше**. Ця панель показує всі деталі обраного файла, а також подробиці свого заслання в. Це дуже зручно, щоб швидко визначити, якщо дублікат дійсно дублікат. Ви також можете двічі клацнути по файлу, щоб відкрити його і пов'язані з ним програми.

Якщо у вас є більше помилкових дублікатів, ніж правда дублікатів (Якщо Ваш фільтр жорсткість дуже низька), кращий спосіб продовжити б переглянути дублікатів, знак істинного дублікати і натисніть **Дії -> Отправить Позначено до кошику** . Якщо у вас є більш вірно, ніж помилкових дублікатів дублікатів, замість цього можна позначити всі файли, які є помилковими дублікатів, а також використовувати **Дії -> Видалити Помічені від результатів**.

Маркування і вибір
---------------------

**Зазначені** дублікат двох примірниках з невеликою прапорець поруч з ним, мають галочки. **Обрано**  дублікат дубліката бути виділені. Кілька дій, вибір може бути виконана в dupeGuru стандартним чином (Shift/Command/Control клік). Ви можете перемикати знак стан всіх вибраних дублікати ", натиснувши **просторі**.

Показати тільки ошукані
-----------------------

Коли цей режим включений, дублікати відображаються без їх відповідного файлу довідки. Ви можете вибрати, марка і сортувати цей список, як і в звичайному режимі.

DupeGuru результати, коли в нормальному режимі, сортуються відповідно до дублікат групи '**посиланням на файл**. Це означає, що якщо ви хочете, наприклад, щоб відзначити все дублікати "EXE" розширенням, ви не можете просто сортувати результати по "Вид", щоб мати всі EXE дублікатів разом, тому що група може складатися з більш ніж одного типу файлів . Ось де обдурені Тільки режим вступає в гру. Щоб позначити всі ваші "EXE" дублікати, ви просто повинні:

* Включити ошукані Тільки режим.
* Додати "Вид" колонку "Стовпці" меню.
* Натисніть на те, що "Вид" колонки, щоб відсортувати список за типом.
* Знайдена перша дублікат з "EXE" роду.
* Виберіть його.
* Перейдіть, щоб знайти останнього дубліката з "EXE" роду.
* Утримуйте Shift і клацніть по ньому.
* Натисніть Space, щоб позначити всі вибрані дублікатів.

Дельта значення
----------------

Якщо включити цей перемикач на деякі стовпці будуть відображати значення по відношенню до дубліката засланні, а не абсолютні значення. Ці дельти значення також будуть відображатися в різні кольори, щоб ви могли помітити їх легко. Наприклад, якщо дублікат 1,2 Мб і своє посилання в 1,4 Мб, розмір стовпець відображає -0,2 Мб.

Тільки ошукані і Дельта значення
--------------------------------

Тільки ошукані режимі розкрити свою дійсну силу, коли ви використовуєте його з Delta Значення перемикач включений. Коли ви дозволите його, відносні значення буде відображатися замість абсолютних. Так що якщо, наприклад, ви хочете видалити з результатів всі дублікати, які є більш 300 Кб від їх посиланню, ви можете відсортувати дублікати тільки результати за розміром, виберіть всі дублікати при -300 в стовпці Розмір, видаляти їх, , а потім зробити те ж саме повторює більше 300 в нижній частині списку.

Ви можете також використовувати його для зміни посилання пріоритет повторювані список. Коли ви робите свіжі сканування, якщо Є немає посилання папки, заслання на файл кожної групи є найбільшою файл. Якщо ви хочете змінити, що, наприклад, в останній модифікації час, ви можете відсортувати дублікати тільки результати за часом модифікації в **убування порядку** , виберіть всі дублікати з часом зміни дельти значення більше 0 і натисніть **Переконайтеся, обраної посилання**. Причина, чому ви повинні зробити порядок сортування за спаданням, тому що якщо 2 файли серед таких же дублікат групи вибираються при натисканні на **Зробити вибраної посилання**, тільки перший із списку будуть зроблені посилання, інші будуть проігноровані . І так як ви хочете Остання зміна файлу для посилання, які мають порядок сортування за спаданням запевняє вас, що першим пунктом у списку буде останньої зміни.

.. todo:: Add "Non-numerical delta" information.

Фільтрація
-----------

dupeGuru підтримує після сканування, фільтрації. З його допомогою ви можете звузити результати, щоб ви могли виконувати дії, на підмножини. Наприклад, ви можете легко помітити всі дублікати з їх ім'я файлу, що містить "копіювати" з результатів за допомогою фільтра.

.. todo:: Qt has a toolbar search field now, not a menu item.

**Windows:** Для використання функції фільтрації, натисніть на Дії -> Застосувати фільтр, запишіть фільтр, який ви хочете застосувати і натисніть ОК. Щоб повернутися до нефільтроване результати, натисніть на Дії -> Скасувати фільтр.

**Mac OS X:** Для використання функції фільтрації, тип фільтра в "Фільтр" поле пошуку на панелі інструментів. Щоб повернутися до нефільтроване результаті, очистіть поле, або натисніть на кнопку "X".

У простому режимі (режим), що ви вводите в якості фільтра рядок, що використовується для виконання фактичної фільтрації, за винятком однієї маски: **\***. Таким чином, якщо ви введете "[*]" як ваш фільтр, він буде відповідати що-небудь з [] дужках в ньому, все, що між цими дужками.

Для більш просунутих фільтрів, ви можете включити «Використання регулярних виразів при фільтрації" на. Функція фільтрації буде використовувати регулярні вирази. Регулярний вираз мови для узгодження тексту. Пояснюючи їх виходить за рамки цього документа. Гарне місце для початку навчання він `регулярного expressions.info <http://www.regular-expressions.info>`__.

Матчі не чутливі до регістру, в простих і регулярних виразів режимі.

Для фільтра, щоб відповідати, регулярний вираз не обов'язково має збігатися цілий файл, він просто зобов'язаний утримувати в ланцюжок, відповідну висловом.

Ви могли помітити, що не всі дублікати в результаті будуть відповідати вашим фільтром. Це тому, що як тільки одна копія в матчах групового фільтра, то вся група залишиться в результатах, таким чином Ви можете мати більш чітке уявлення про дубліката контексті. Тим не менш, не відповідні дублікати у "заслання режимі". Таким чином, можна виконувати дії, як Марк все і обов'язково тільки знак фільтрується дублікатів.

Дія меню
-----------

* **Відкритий чорний список:** Видаліть всі ігнорують матчі ви додали. Ви повинні почати новий пошук знову очищується список ігнорованих щоб бути ефективними.
* **Експорт результатів в XHTML:** Візьміть поточні результати, а також створювати файл XHTML з нього. Стовпців, які видно при натисканні на цю кнопку буде стовпців у файлі XHTML. Файл автоматично відкриється в браузері за замовчуванням.
* **Надіслати Позначено в кошику:** Відправити всі відмічені дублікати, сміття, це очевидно.
* **Видалити Помічені і заміна з Жорсткі**: Передає всі відмічені дублікати, сміття, але після того, як зробили це, вилучені файли замінюються `жорстких <http://en.wikipedia.org/wiki/Hard_link>`__ посилання до заслання на файл. (Тільки для OS X і Linux)
* **Переміщення Позначено в ...:** запросить призначення, а потім перемістити всі відмічені файли в тому, що призначення. Шлях вихідного файлу може бути відтворений в пункт призначення, залежно від "Копіювання і переміщення" переваги.
* **Скопіюйте Позначено в ...:** запитає у вас місце, а потім скопіювати всі вибрані файли до цього пункту призначення. Шлях вихідного файлу може бути відтворений в пункт призначення, залежно від "Копіювання і переміщення" переваги.
* **Видалити Помічені з результатів:** Видалити все відмічені дублікатів з результату пошуку. Самі файли не будуть порушені й залишаться, де вони.
* **Видалити вибрані з результатів:** Видалити всі вибрані дублікатів з результату пошуку. Зверніть увагу, що всі вибрані файли посилання будуть ігноруватися, тільки дублікати можуть бути видалені з цією дією.
* **Зробити Обраний Довідка:** Сприяння всі вибрані дублікатів посилання. Якщо дублікат частиною групи, що має посиланням на файл найближчі із заслання папки (в синій колір), не будуть прийняті заходи для цього дублікат. Якщо більш ніж один дублікат серед тієї ж групи обрані, тільки перший з кожної групи буде заохочуватися.
* **Додати обрані в чорний список:** Це спочатку видаляє всі вибрані дублікати з результатів, а потім додати матчу, які дублюють та опорний струм в чорний список. Цей матч не прийде знову в подальшої перевірки. Копіювати себе і, можливо, повернеться, але він буде шукатися в іншій посиланням на файл. Ви можете очистити список ігнорованих з Відкритий чорний список команди.
* **Відкрите Обраний з додатків за замовчунням:** Відкрийте файл за допомогою програми, пов'язаного з типом обраного файлу.
* **Розкривати Обраний в Finder:** Відкрийте папку, яка містить вибраний файл.
* **Викликати спеціальної команди:** Викликає зовнішню програму ви встановили в настройках з використанням виділеного фрагмента в якості аргументів у виклику.
* **Перейменування обрано:** Запит нове ім'я, а потім перейменувати вибраний файл.

.. todo:: Add Move and iPhoto/iTunes warning
.. todo:: Add "Deletion Options" section.
