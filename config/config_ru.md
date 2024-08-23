## Типы данных

Каждая опция может принимать только определенный тип данных:

- **bool**: Логическое значение, где `true` означает ДА, а `false` - НЕТ.
- **int**: Целые числа, например, `1`, `2` и т.д.
- **float**: Числа с плавающей точкой, например, `1.2`, `1.22`, `1.2345` и т.д.
- **str**: Строки, например, `text`.

## Настройки

### Разрешение окна поиска объектов

Это окно используется для поиска предметов и расположено в центре экрана. Маленький размер окна повышает производительность, избегая поиска в полноэкранном режиме. Стандартный размер окна - 384x216 пикселей, что составляет 20% от разрешения экрана 1920x1080. Увеличение размера окна может повысить нагрузку на вычислительные ресурсы.

- **detection_window_width** `int`: Ширина окна поиска объектов в пикселях.
- **detection_window_height** `int`: Высота окна поиска объектов в пикселях.

![Object Search Window](https://github.com/SunOner/sunone_aimbot_docs/blob/main/config/media/object_search_window.png)

### Метод захвата Bettercam

[Bettercam](https://github.com/RootKit-Org/BetterCam) - это сторонняя библиотека для захвата изображений с экрана, работающая на том же API, что и Geforce Experience. По умолчанию работает на 60 кадрах в секунду. Для динамичных игр рекомендуется увеличить частоту до 100 кадров в секунду.

- **Bettercam_capture** `bool`: `true` - использовать Bettercam для захвата, `false` - не использовать.
- **bettercam_capture_fps** `int`: Частота кадров в секунду.
- **bettercam_monitor_id** `int`: ID монитора для захвата (`0` для основного монитора).
- **bettercam_gpu_id** `int`: ID видеокарты для захвата (`0` для основной видеокарты).

### Метод захвата OBS

Захват с помощью [OBS](https://github.com/obsproject/obs-studio).

#### Настройка OBS

1. Добавьте источник захвата окна/игры.
2. Перейдите в настройки OBS:
   - **Вывод**:
     - Кодировщик видео: NVIDIA NVENC H.264.
     - Масштабировать вывод: 568x320 (примерный размер).
   - **Видео**:
     - Базовое разрешение: 568x320.
     - Разрешение выхода: 568x320.
     - Частота кадров: 60.
   - **Расширенные**:
     - Приоритет процесса: Выше среднего или Высокий.
     - Настройка CUDA и OpenGL для второй видеокарты через панель управления Nvidia.

3. В окне предпросмотра уменьшите изображение до 568x320.
4. Выровняйте изображение по центру с помощью CTRL+D.
5. Нажмите `Запустить виртуальную камеру`.

- **Obs_capture** `bool`: `true` - использовать OBS для захвата, `false` - не использовать.
- **Obs_camera_id** `str` or `int`: `auto` для автоматического поиска камеры или вручную введите ID.
- **Obs_capture_fps** `int`: Частота кадров для захвата.

### Aim (Прицеливание)

- **body_y_offset** `float`: Смещение по оси Y, если голова не найдена или отключено наведение на голову. Например, `0.35` для смещения вверх.
![Aim Diagram](https://github.com/SunOner/sunone_aimbot_docs/blob/main/config/media/body_y_offset.png)
- **hideout_targets** `bool`: `true` - включить наведение на мишени, `false` - выключить.
- **disable_headshot** `bool`: `true` - отключить наведение на голову, `false` - включить.
- **disable_prediction** `bool`: `true` - отключить предсказание позиции цели, `false` - включить.
- **prediction_interval** `float`: Интервал предсказания цели.
- **third_person** `bool`: `true` - игнорировать игрока от третьего лица, `false` - не игнорировать.

### Горячие клавиши

- **hotkey_targeting** `str`: Клавиша для наведения на цель. Поддерживает несколько кнопок, например, `RightMouseButton,X2MouseButton`.
- **hotkey_exit** `str`: Клавиша для выхода из программы. По умолчанию `F2`.
- **hotkey_pause** `str`: Клавиша для паузы. По умолчанию `F3`.
- **hotkey_reload_config** `str`: Клавиша для перезагрузки конфигурации. По умолчанию `F4`.

### Мышь

- **mouse_dpi** `int`: DPI программной мыши.
- **mouse_sensitivity** `float`: Чувствительность мыши.
- **mouse_fov_width** `int`: Горизонтальный угол обзора.
- **mouse_fov_height** `int`: Вертикальный угол обзора.
- **mouse_min_speed_multiplier** `float`: Минимальный множитель скорости.
- **mouse_max_speed_multiplier** `float`: Максимальный множитель скорости.
- **mouse_lock_target** `bool`: `true` - захват цели без удержания кнопки, `false` - удерживать кнопку.
- **mouse_auto_aim** `bool`: `true` - автоматическое наведение, `false` - ручное.

#### Драйверы для мыши

- **mouse_ghub** `bool`: Использовать эксплойт Logitech GHUB. Требуется [GHUB](https://disk.yandex.ru/d/LagJI9dR-kM9cQ).
- **mouse_rzr** `bool`: Для мышек Razer. Требуется [synapse 3](https://www.razer.com/synapse-3).

### Стрельба

- **auto_shoot** `bool`: Включить автоматическую стрельбу.
- **triggerbot** `bool`: Автоматическая стрельба при наведении на цель.
- **force_click** `bool`: `true` - стрелять даже вне зоны прицела, `false` - только в зоне.
- **bScope_multiplier** `float`: Множитель зоны для автоматической стрельбы.

### Arduino

- **arduino_move** `bool`: `true` - отправлять команды передвижения на Arduino.
- **arduino_shoot** `bool`: `true` - отправлять команды стрельбы на Arduino.
- **arduino_port** `str`: COM порт Arduino (`COM1`, `COM2` или `auto`).
- **arduino_baudrate** `int`: Скорость передачи данных.
- **arduino_16_bit_mouse** `bool`: `true` - использовать 16-битные значения для мыши.

### Искусственный интеллект (AI)

- **AI_model_name** `str`: Название модели ИИ.
- **AI_model_image_size** `int`: Размер изображения для модели ИИ.
- **AI_conf** `float`: Уровень уверенности ИИ для наведения.
- **AI_device** `int` or `str`: Устройство для вычислений (`0`, `1` или `cpu`).
- **AI_enable_AMD** `bool`: `true` - использовать устройства AMD.
- **AI_mouse_net** `bool`: Использовать нейронные сети для передвижения мыши.

### Оверлей

- **show_overlay** `bool`: Включить оверлей.
- **overlay_show_borders** `bool`: Показать границы оверлея.
- **overlay_show_boxes** `bool`: Показать найденные цели.
- **overlay_show_target_line** `bool`: Показать линии до цели.
- **overlay_show_target_prediction_line** `bool`: Показать линию предсказания.
- **overlay_show_labels** `bool`: Показать имена целей.
- **overlay_show_conf** `bool`: Показать уровень уверенности.

### Окно отладки

- **show_window** `bool`: Показать окно отладки.
- **show_detection_speed** `bool`: Показать скорость работы ИИ.
- **show_window_fps** `bool`: Показать FPS окна.
- **show_boxes** `bool`: Показать найденные объекты.
- **show_labels** `bool`: Показать имена объектов.
- **show_conf** `bool`: Показать уровень уверенности.
- **show_target_line** `bool`: Показать линию до цели.
- **show_target_prediction_line** `bool`: Показать линию предсказания.
- **show_bScope_box** `bool`: Показать зону для автовыстрела.
- **show_history_points** `bool`: Показать историю передвижения мыши.
- **debug_window_always_on_top** `bool`: Окно отладки всегда поверх других окон.
- **spawn_window_pos_x** `int`: X координата окна отладки.
- **spawn_window_pos_y** `int`: Y координата окна отладки.
- **debug_window_scale_percent** `int`: Размер окна отладки в процентах.

Имя окна отладки выбирается случайно из файла `window_names.txt`.