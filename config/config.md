## Logical Data Types
Each option can only accept a specific data type:
- bool: `true` meaning YES or `false` meaning NO.
- int: Only whole numbers like `1`, `2`, etc.
- float: Only numbers with a decimal point like `1.2`, `1.22`, `1.2345`, etc.
- str: String `text`.

### Object Search Window Resolution:
This is the window where item search is conducted. It is small in size and located in the center of the screen. The small window size is needed to increase computational performance and avoid searching for objects in full-screen mode. The standard window options at 384x216 are 20% of the screen resolution of 1920x1080. The larger the window size, the more computational operations will be performed.
- detection_window_width `int`: The width of the object search window in pixels.
- detection_window_height `int`: The height of the object search window in pixels.

![Object Search Window](https://github.com/SunOner/sunone_aimbot_docs/blob/main/config/media/object_search_window.png)

### Bettercam Capture Method:
[This is a third-party library](https://github.com/RootKit-Org/BetterCam) for capturing images from the screen. It operates on the same API as Geforce Experience for video recording. It has a default value of 60 frames per second. If the game has very dynamic gameplay, it is recommended to increase the frames per second to 100.
- Bettercam_capture `bool`: `true` - use this method for image capture, `false` do not use this method.
- bettercam_capture_fps `int`: `60` frames per second.
- bettercam_monitor_id `int`: If you want to use screen recording from the main monitor, set the value to `0`; another monitor has a value higher than `1`, `2`, etc.
- bettercam_gpu_id `int`: Which graphics card will be used for image capture, `0` is the default GPU ID, i.e., installed in the first PCI slot, `1`, `2`, etc.

### OBS Capture Method:
Capture method using the [OBS](https://github.com/obsproject/obs-studio) program.
- OBS Setup.
	- Add a window/game capture source.
	- Go to OBS settings.
	- Output tab.
		- Video encoder: NVIDIA NVENC H.264.
		- Scale output (checkbox): 568x320. (This is an approximate size, it can be different as per your preference.)
	- Video tab.
		- Base resolution: 568x320.
		- Output resolution (scaled): 568x320.
		- Common FPS values: 60.
	- Advanced tab (additional options).
		- Process priority: Above normal or High.
		- If you have a second graphics card (for example, my second monitor is connected via GTX 1080, and the main graphics card is RTX 3080ti).
			- Go to Nvidia Control Panel > 3D Settings > Manage 3D Settings > Program Settings > And add OBS.
			- In functions:
			- CUDA - GPUs: Use only these GPUs: GTX 1080.
			- OpenGL rendering GPU: Use only these GPUs: GTX 1080.
			- Apply.
	- In the preview window, reduce the image by clicking on the source and pressing the CTRL+E key combination, reduce it to 568x320.
	- To center the image, press the CTRL+D key combination.
	- Now click `Start Virtual Camera`.

- Obs_capture `bool`: `true` - use this method for image capture, `false` do not use this method.
- Obs_camera_id `str` or `int`: Enter the value `auto` for the program to automatically find the OBS virtual camera, or manually enter the virtual camera ID `0`, `1`, etc.
- Obs_capture_fps `int`: Specific fps value for screen capture.

### Aim:
- body_y_offset `float`: Offset the coordinates on the Y-axis (up from the target) by `0.35` if the head was not found or the head targeting function was disabled. `0.00` is the center of the target, you can also use `-0.10`, etc.
<br></br>
> [!NOTE]
> Pay attention to the image. At the first, the player is detected by half and if the value is set to 0.50, the aimbot will be aimed at the head. In the second image, the player is completely detected, and if the value is set to the same 0.50, then the shots will no longer be fired into the head but into the chest.

![Aim Diagram](https://github.com/SunOner/sunone_aimbot_docs/blob/main/config/media/body_y_offset.png)
- hideout_targets `bool`: The AI model distinguishes targets on the range. `true` enable targeting on targets, `false` disable.
- disable_headshot `bool`: `true` disable head targeting, `false` target the head.
- disable_prediction `bool`: If set to `true`, the prediction of the target's position on the next frame will not be performed, `false` use target predictions. Useful for targeting moving targets.
- prediction_interval `float`: The higher the value, the faster the target prediction function will be processed.
- third_person `bool`: `true` - the AI model will ignore the third-person player, `false` - the third-person player will not be ignored and the aimbot will target them.

### Hot Keys:
- You can view all the keys that can be used [here](https://github.com/SunOner/sunone_aimbot/blob/main/logic/buttons.py). Enter the value `None` to deactivate the function. All key presses are registered even when the program is minimized.
- hotkey_targeting `str`: Targeting. Supports multiple buttons, for example, `hotkey_targeting = RightMouseButton,X2MouseButton` (without spaces, separated by commas). Default is `right mouse button`.
- hotkey_exit `str`: Exit the program. Default key is `F2`.
- hotkey_pause `str`: Pause the aimbot. Default button is `F3`.
- hotkey_reload_config `str`: Reloads and applies new config settings if they were changed. Default button is `F4`.

### Mouse:
- mouse_dpi `int`: DPI of the software mouse. The higher the DPI, the faster it will move.
- mouse_sensitivity `float`: The value by which to divide the mouse coordinates, works as mouse sensitivity, for example, if the value is set to `2`, the coordinates will be divided by 2 and the mouse will move slower.
- mouse_fov_width `int`: Horizontal field of view from the game, improves aiming.
- mouse_fov_height `int`: Vertical field of view from the game, improves aiming.
- mouse_min_speed_multiplier `float`: Minimum mouse movement speed multiplier. Allows the mouse to gain minimum speed.
- mouse_max_speed_multiplier `float`: Maximum mouse movement speed multiplier. Prevents the mouse from gaining too much speed.
- mouse_lock_target `bool`: If set to `true`, the target will be locked without holding the mouse button, press the button again to release the target. Set to `false` to require holding the button for targeting.
- mouse_auto_aim `bool`: If set to `true`, the aimbot will aim without pressing the targeting button, `false` aim using mouse buttons.
- Some games block software mouse input, for this there are built-in drivers:
	- mouse_ghub `bool`: If set to `true`, the Logitech GHUB exploit will be used for mouse input. Requires installing a specific version of the [GHUB](https://disk.yandex.ru/d/LagJI9dR-kM9cQ) program and not updating it as the exploit only works on the old version. Suitable not only for Logitech mice. `false` do not use the function.
	- mouse_rzr `bool`: Only for Razer mice. Requires installing [synapse 3](https://www.razer.com/synapse-3), after installation go to the modules tab and install `macro`.

### Shooting:
- auto_shoot `bool`: Enable automatic shooting. (For some games, [arduino](https://github.com/SunOner/HID_Arduino), GHUB exploit, or Razer is required).
- triggerbot `bool`: When the target is in sight, performs automatic shooting, requires the `mouse_auto_shoot` option to be enabled, and auto-aiming will be disabled.
- force_click `bool`: `true` shoot even when the target is not in the aiming zone, `false` shoot only when the target is in the aiming zone.
- bScope_multiplier `float`: Allows increasing or decreasing the player's zone (box) for automatic shooting. `1.00` - Standard value, `2.20` - enlarged zone, `0.50` - reduced zone.

### Arduino:
- arduino_move `bool`: `true` to send mouse movement commands to Arduino. `false` not to send.
- arduino_shoot `bool`: `true` to send mouse button press commands to Arduino for automatic fire. `false` not to send.
- arduino_port `str`: COM port of Arduino. Use values `COM1`, `COM2` to manually determine the Arduino port, or `auto` for the aimbot to find it automatically.
- arduino_baudrate `int`: Baudrate of Arduino, the higher the value, the faster the commands will be processed.
- arduino_16_bit_mouse `bool`: `true` send 16-bit values to the port for mouse movement (coordinate range increases to -32768 - 32768), works if the mouse supports them. `false` send 8-bit values for mouse movement (range -127 - 127).

### AI:
- AI_model_name `str`: The name of the AI model that will be used for object detection. Models are located in the `./models` folder. For example, `AI_model_name = sunxds_0.5.6.pt`.
- AI_model_image_size `int`: Image size of the AI model. Each model has its own image size used during training. Using a different image size may result in incorrect targeting and performance. Authors always specify the image size of the AI model when they publish it somewhere.
- AI_conf `float`: How confident the AI should be to target an object. For example, a value of `0.20`, if the AI sees a player with confidence greater than or equal to 20%, it will target them. The higher the value, the fewer players may be found and vice versa.
- AI_device `int` or `str`: On which device to perform computations for object detection, integers are GPU devices (graphics card) like `0`, `1`, etc. You can use the processor for computations with the value `cpu`, but performance will be weak.
- AI_enable_AMD `bool`: `true` to use AMD devices. Requires installation of ROCm, [Zluda](https://github.com/vosen/ZLUDA), and a version of PyTorch for AMD. See [AMD documentation](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/how-to/install.html) and [Zluda](https://github.com/vosen/ZLUDA) to learn how to run Python code on AMD.
- AI_mouse_net `bool`: Use neural networks for mouse movement. See [this repository](https://github.com/SunOner/mouse_net).

### Overlay:
> [!NOTE]
> Not recommended for gaming as the interface is drawn over all applications and is clickable. Also, some games automatically take screenshots to check players for fair play.

- show_overlay `bool`: Enable overlay.
- overlay_show_borders `bool`: Draw overlay borders.
- overlay_show_boxes `bool`: Draw found targets.
- overlay_show_target_line `bool`: Draw lines from the center of the screen to the target.
- overlay_show_target_prediction_line `bool`: Draw prediction line from the center of the screen to the target.
- overlay_show_labels `bool`: Display target names.
- overlay_show_conf `bool`: Display target names and confidence level.

### Debug Window:
- show_window `bool`: Display the debug window.
- show_detection_speed `bool`: Display information about the AI model's speed in the debug window.
- show_window_fps `bool`: Display the number of frames per second of screen recording.
- show_boxes `bool`: Display found objects.
- show_labels `bool`: Display names of found objects.
- show_conf `bool`: Display confidence percentage of found objects.
- show_target_line `bool`: Display the mouse movement line from the center of the screen to the found target.
- show_target_prediction_line `bool`: Display the prediction line from the center of the screen to the found target.
- show_bScope_box  `bool`: Display the target box necessary for auto-shooting.
- show_history_points `bool`: Display mouse movement history points.
- debug_window_always_on_top `bool`: When enabled, the debug window will be displayed on top of other windows.
- spawn_window_pos_x `int`: X coordinate of the debug window's appearance when the aimbot starts.
- spawn_window_pos_y `int`: Y coordinate of the debug window's appearance when the aimbot starts.
- debug_window_scale_percent `int`: Size of the debug window in percent.
- The name of the debug window is randomly selected from the window_names.txt file.