## Logical Data Types
Each option can only accept a specific data type:
- `bool`: `true` meaning YES or `false` meaning NO.
- `int`: Only whole numbers like `1`, `2`, etc.
- `float`: Only numbers with a decimal point like `1.2`, `1.22`, `1.2345`, etc.
- `double`: `0.20`, `0.99` or `0.01`.
- `str`: String `text`.

### Capture
These are the settings for the main window where object detection occurs. The window is small and located in the center of the screen. The small window size is necessary to reduce system load and prevent objects from being detected across the entire screen.
- capture_method `str`: The screen capture method. Choose between `duplication_api`, `winrt`, or `virtual_camera` options.
- detection_resolution: `int`: Resolution of the window in pixels. For example, a value of `400` will set the window resolution to 400 horizontally and 400 vertically.
- capture_fps `float`: Frames per second limiter for window recording. The higher this value, the faster the detection rate, but keep in mind that CPU load might also increase. To disable FPS limiting, set the value to `0.0`.
- monitor_idx `int`: The ID of the monitor on which the screen capture will be performed. `0` is the main monitor.
- circle_mask `bool`: Enable circle mask overlay. Useful for third-person shooters to hide the character.
- capture_borders `bool`: Enable the display of recording boundary frames. (Requires Windows 10 version 1809 or higher)
- capture_cursor `bool`: Display the mouse cursor during recording. (Requires Windows 10 version 1809 or higher)
- virtual_camera_name `str`: The name of the virtual camera. It is applied automatically.

### Target
- disable_headshot `bool`: Disable targeting heads.
- body_y_offset `float`: Offset the coordinates on the Y-axis (up from the target) by `0.35` if the head was not found or the head targeting function was disabled. `0.00` is the center of the target; you can also use `-0.10`, etc.
  
  > [!NOTE]
  > Pay attention to the image. Initially, the player is detected by half, and if the value is set to 0.50, the aimbot will aim at the head. In the second image, the player is completely detected, and if the value is set to the same 0.50, then the shots will not be aimed at the head but at the chest.
  
- ignore_third_person `bool`: `true` - the AI model will ignore the third-person player, `false` - the third-person player will not be ignored, and the aimbot will target them.
- shooting_range_targets `bool`: Turn on target guidance at the shooting range.
- auto_aim `bool`: The aimbot will automatically target the enemy without pressing any buttons.

### Mouse move
- dpi `int`: DPI of the software mouse. The higher the DPI, the faster it will move.
- sensitivity `float`: The value by which to divide the mouse coordinates, works as mouse sensitivity. For example, if the value is set to `2`, the coordinates will be divided by 2, and the mouse will move slower.
- fovX `int`: Horizontal field of view from the game, improves aiming.
- fovY `int`: Vertical field of view from the game, improves aiming.
- minSpeedMultiplier `float`: Minimum mouse movement speed multiplier. Allows the mouse to gain minimum speed.
- maxSpeedMultiplier `float`: Maximum mouse movement speed multiplier. Prevents the mouse from gaining too much speed.
- predictionInterval `float`: The higher the value, the faster the target prediction function will be processed.
- easynorecoil `bool`: Enable easy no-recoil.
- easynorecoilstrength `float`: How much does the crosshair pull down when the easynorecoil option is enabled?
- input_method `str`: Mouse input method. WIN32 / [GHUB](https://github.com/SunOner/sunone_aimbot_docs/blob/main/tips/ghub.md) / [ARDUINO](https://github.com/SunOner/HID_Arduino)

### Arduino
- arduino_baudrate `int`: Baudrate of Arduino, the higher the value, the faster the commands will be processed.
- arduino_port `str`: COM port of Arduino. Use values `COM1`, `COM2` to manually determine the Arduino port, or `auto` for the aimbot to find it automatically.
- arduino_16_bit_mouse `bool`: `true` sends 16-bit values to the port for mouse movement (coordinate range increases to `-32768` - `32768`), works if the mouse supports them. `false` sends 8-bit values for mouse movement (range `-127` - `127`).
- arduino_enable_keys `bool`: When the targeting button is pressed, data from Arduino is forwarded to the aimbot (button pressed/released) and triggers the auto-targeting function. It is useful for applications that do not allow the application to recognize whether a button has been pressed.

### Mouse shooting
- auto_shoot `bool`: Enable automatic shooting. (For some games, [arduino](https://github.com/SunOner/HID_Arduino), GHUB exploit, or Razer is required).
- bScope_multiplier `float`: Allows increasing or decreasing the player's zone (box) for automatic shooting. `1.00` - Standard value, `2.20` - enlarged zone, `0.50` - reduced zone.

### AI
- ai_model `str`: The name of the AI model that will be used for object detection. Models are located in the `./models` folder. For example, `AI_model_name = sunxds_0.5.6.pt`.
- confidence_threshold `float`: How confident the AI should be to target an object. For example, a value of `0.20`, if the AI sees a player with confidence greater than or equal to 20%, it will target them. The higher the value, the fewer players may be found, and vice versa.
- nms_threshold `float`: This function analyzes detections from a single frame, and if the boxes are roughly on the same object, it merges them into one box.
- max_detections `int`: The maximum number of objects that can be detected per frame.
- postprocess `str`: Which model parsing method to use. Choose between `yolo8`, `yolo9`, `yolo10`, `yolo11` or `yolo12`.
- export_enable_fp8 `bool`: Export the model with FP8 quantization. The model will run faster, but accuracy will drop by about 4% (not supported by all GPUs). Disabled by default.
- export_enable_fp16 `bool`: Export the model with FP16 quantization. The model will run faster.

### CUDA
- use_cuda_graph `bool`: The function is under development. Currently, it doesn't respond to anything.
- use_pinned_memory `bool`: Enable data transfer acceleration between CPU and GPU. (Not supported on all GPUs)

### Optical Flow
At the moment (version 2.8) this option is under development. In the future, it can be used to dampen the recoil of weapons or improve motion prediction. It doesn't affect anything right now.
- enable_optical_flow `bool`: Turn on or off the optical flow.
- draw_optical_flow `bool`: Draw the optical flow in the debugging window.
- draw_optical_flow_steps `int`: The size of the rendering grid.
- optical_flow_alpha_cpu `float`: The size of the alpha channel during flow conversion.
- optical_flow_magnitudeThreshold `double`: Optical flow correction.
- staticFrameThreshold `float`: If the frames do not differ from each other, then the value will be the lowest. Set the value to a higher value so that you do not process identical frames.

### Buttons
You can view all the keys that can be used [here](https://github.com/SunOner/sunone_aimbot_cpp/blob/main/sunone_aimbot_cpp/keyboard/keycodes.cpp). Enter the value `None` to deactivate the function. All key presses are registered even when the program is minimized. It supports multiple keys, for example, `button_targeting = RightMouseButton, MiddleMouseButton`.

- button_targeting `str`: Targeting.
- button_shoot `str`: Shoot button for easy anti recoil option.
- button_zoom `str`: Zoom button for easy anti recoil option.
- button_exit `str`: Exit the program.
- button_pause `str`: Pause the program.
- button_reload_config `str`: Reload the config.
- button_open_overlay `str`: Open the overlay. It doesn't work with applications running in full-screen mode.

### Overlay
- overlay_opacity `int`: The transparency value of the overlay. Values from `1` to `255` are accepted.
- overlay_snow_theme `bool`: Switching on and off the winter theme.
- overlay_ui_scale `float`: Change global UI scale of overlay.

### Custom Classes
Below are the class redistribution settings. These settings are useful for those who are not working with the original model. For example, if you load your own model and it has only 2 classes: `player` and `head`. To enable the program to process these values and distinguish between the head and the player, do the following:

```python
class_player = 0
class_bot = 99
class_weapon = 99
class_outline = 99
class_dead_body = 99
class_hideout_target_human = 99
class_hideout_target_balls = 99
class_head = 1
class_smoke = 99
class_fire = 99
class_third_person = 99
```

As you can see, I have reassigned the indices for the player and head classes. For the other classes, I have set the values to 99 because such an index definitely does not exist in the model, and it functions as None/NULL.

### Debug window
- show_window `bool`: Display the debug window.
- show_fps `bool`: Display the number of frames per second of screen recording.
- window_name `str`: Name of the debug window.
- window_size `int`: Size of the debug window in percent.
- debug_window_screenshot_key `str`: Take a screenshot of the [button](https://github.com/SunOner/sunone_aimbot_cpp/blob/main/sunone_aimbot_cpp/keyboard/keycodes.cpp) from the debug screen. The screenshot will be saved to the screenshots directory. It is useful for training and retraining models.
- screenshot_delay `int`: If the screenshot button is held down, it takes screenshots every N milliseconds. Useful if the button is set as the shooting button `debug_window_screenshot_key = RightMouseButton`.
- always_on_top `bool`: When enabled, the debug window will be displayed on top of other windows.
- verbose`bool`: Enable detailed output in the console.