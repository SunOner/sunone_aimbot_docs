## Logical Data Types
Each option can only accept a specific data type:
- bool: `true` meaning YES or `false` meaning NO.
- int: Only whole numbers like `1`, `2`, etc.
- float: Only numbers with a decimal point like `1.2`, `1.22`, `1.2345`, etc.
- str: String `text`.

### Capture
These are the settings for the main window where object detection occurs. The window is small and located in the center of the screen. The small window size is necessary to reduce system load and prevent objects from being detected across the entire screen. If the `duplication_api` option is disabled, the capture method from the standard Windows libraries `WinRT` is used. When using this library, mouse and border display functions become available during recording. Some users may find that disabling mouse or border recording options causes the application to close, so use the `duplication_api` method for these cases.
- detection_resolution: `int`: Resolution of the window in pixels. For example, a value of `400` will set the window resolution to 400 horizontally and 400 vertically.
- capture_fps `float`: Frames per second limiter for window recording. The higher this value, the faster the detection rate, but keep in mind that CPU load might also increase. To disable FPS limiting, set the value to `0.0`.
- capture_borders `bool`: Enable the display of recording boundary frames.
- capture_cursor `bool`: Display the mouse cursor during recording.
- duplication_api `bool`: Use the `windows duplication api` for recording.

### Target
- disable_headshot `bool`: Disable targeting heads.
- body_y_offset `float`: Offset the coordinates on the Y-axis (up from the target) by `0.35` if the head was not found or the head targeting function was disabled. `0.00` is the center of the target; you can also use `-0.10`, etc.
  
  > [!NOTE]
  > Pay attention to the image. Initially, the player is detected by half, and if the value is set to 0.50, the aimbot will aim at the head. In the second image, the player is completely detected, and if the value is set to the same 0.50, then the shots will not be aimed at the head but at the chest.
  
- ignore_third_person `bool`: `true` - the AI model will ignore the third-person player, `false` - the third-person player will not be ignored, and the aimbot will target them.

### Mouse move
- dpi `int`: DPI of the software mouse. The higher the DPI, the faster it will move.
- sensitivity `float`: The value by which to divide the mouse coordinates, works as mouse sensitivity. For example, if the value is set to `2`, the coordinates will be divided by 2, and the mouse will move slower.
- fovX `int`: Horizontal field of view from the game, improves aiming.
- fovY `int`: Vertical field of view from the game, improves aiming.
- minSpeedMultiplier `float`: Minimum mouse movement speed multiplier. Allows the mouse to gain minimum speed.
- maxSpeedMultiplier `float`: Maximum mouse movement speed multiplier. Prevents the mouse from gaining too much speed.
- predictionInterval `float`: The higher the value, the faster the target prediction function will be processed.

### Ghub
- ghub `bool`: If set to `true`, the Logitech GHUB exploit will be used for mouse input. [GHUB install guide](https://github.com/SunOner/sunone_aimbot_docs/blob/main/tips/ghub.md).

### Arduino
- arduino_enable `bool`: Send mouse movement data to Arduino. Instructions can be found [here](https://github.com/SunOner/HID_Arduino).
- arduino_baudrate `int`: Baudrate of Arduino, the higher the value, the faster the commands will be processed.
- arduino_port `str`: COM port of Arduino. Use values `COM1`, `COM2` to manually determine the Arduino port, or `auto` for the aimbot to find it automatically.
- arduino_16_bit_mouse `bool`: `true` sends 16-bit values to the port for mouse movement (coordinate range increases to `-32768` - `32768`), works if the mouse supports them. `false` sends 8-bit values for mouse movement (range `-127` - `127`).
- arduino_enable_keys `bool`: (experimental) When the targeting button is pressed, data from Arduino is forwarded to the aimbot (button pressed/released) and triggers the auto-targeting function.

### Mouse shooting
- auto_shoot `bool`: Enable automatic shooting. (For some games, [arduino](https://github.com/SunOner/HID_Arduino), GHUB exploit, or Razer is required).
- bScope_multiplier `float`: Allows increasing or decreasing the player's zone (box) for automatic shooting. `1.00` - Standard value, `2.20` - enlarged zone, `0.50` - reduced zone.

### AI
- ai_model `str`: The name of the AI model that will be used for object detection. Models are located in the `./models` folder. For example, `AI_model_name = sunxds_0.5.6.pt`.
- engine_image_size `int`: Image size of the AI model. Each model has its own image size used during training. Using a different image size may result in incorrect targeting and performance. Authors always specify the image size of the AI model when they publish it somewhere.
- confidence_threshold `float`: How confident the AI should be to target an object. For example, a value of `0.20`, if the AI sees a player with confidence greater than or equal to 20%, it will target them. The higher the value, the fewer players may be found, and vice versa.
- nms_threshold `float`: This function analyzes detections from a single frame, and if the boxes are roughly on the same object, it merges them into one box.

### Buttons
You can view all the keys that can be used [here](https://github.com/SunOner/sunone_aimbot_cpp/blob/main/sunone_aimbot_cpp/scr/keycodes.cpp). Enter the value `None` to deactivate the function. All key presses are registered even when the program is minimized. It supports multiple keys, for example, `button_targeting = RightMouseButton, MiddleMouseButton`.
- button_targeting `str`: Targeting.
- button_exit `str`: Exit the program.
- button_pause `str`: Pause the program.
- button_reload_config `str`: Reload the config.
- button_open_overlay `str`: Open the overlay. It doesn't work with applications running in full-screen mode.

### Overlay
- overlay_opacity `int`: The transparency value of the overlay. Values from `1` to `255` are accepted.

### Debug window
- show_window `bool`: Display the debug window.
- show_fps `bool`: Display the number of frames per second of screen recording.
- window_name `str`: Name of the debug window.
- window_size `int`: Size of the debug window in percent.
- debug_window_screenshot_key `str`: Take a screenshot of the [button](https://github.com/SunOner/sunone_aimbot_cpp/blob/main/sunone_aimbot_cpp/scr/keycodes.cpp) from the debug screen. The screenshot will be saved to the screenshots directory. It is useful for training and retraining models.
- screenshot_delay `int`: If the screenshot button is held down, it takes screenshots every N milliseconds. Useful if the button is set as the shooting button `debug_window_screenshot_key = RightMouseButton`.
- always_on_top `bool`: When enabled, the debug window will be displayed on top of other windows.