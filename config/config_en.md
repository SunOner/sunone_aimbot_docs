## Data Types

Each option can only accept a specific data type:

- **bool**: A boolean value, where `true` means YES and `false` means NO.
- **int**: Integer numbers, such as `1`, `2`, etc.
- **float**: Floating-point numbers, such as `1.2`, `1.22`, `1.2345`, etc.
- **str**: Strings, such as `text`.

## Settings

### Object Search Window Resolution

This window is used for searching items and is located at the center of the screen. A smaller window size improves performance by avoiding full-screen search. The standard window size is 384x216 pixels, which is 20% of a 1920x1080 screen resolution. Increasing the window size may increase the load on computing resources.

- **detection_window_width** `int`: Width of the object search window in pixels.
- **detection_window_height** `int`: Height of the object search window in pixels.

![Object Search Window](https://github.com/SunOner/sunone_aimbot_docs/blob/main/config/media/object_search_window.png)

### Bettercam Capture Method

[Bettercam](https://github.com/RootKit-Org/BetterCam) is a third-party library for capturing images from the screen, operating on the same API as Geforce Experience. By default, it runs at 60 frames per second. For dynamic games, it is recommended to increase the rate to 100 frames per second.

- **Bettercam_capture** `bool`: `true` to use Bettercam for capture, `false` not to use it.
- **bettercam_capture_fps** `int`: Frames per second.
- **bettercam_monitor_id** `int`: Monitor ID for capture (`0` for the primary monitor).
- **bettercam_gpu_id** `int`: GPU ID for capture (`0` for the primary GPU).

### OBS Capture Method

Capture using [OBS](https://github.com/obsproject/obs-studio).

#### OBS Setup

1. Add a window/game capture source.
2. Go to OBS settings:
   - **Output**:
     - Video encoder: NVIDIA NVENC H.264.
     - Scale output: 568x320 (approximate size).
   - **Video**:
     - Base resolution: 568x320.
     - Output resolution: 568x320.
     - Frame rate: 60.
   - **Advanced**:
     - Process priority: Above normal or High.
     - Configure CUDA and OpenGL for the second GPU via the Nvidia control panel.

3. In the preview window, reduce the image to 568x320.
4. Center the image using CTRL+D.
5. Click `Start Virtual Camera`.

- **Obs_capture** `bool`: `true` to use OBS for capture, `false` not to use it.
- **Obs_camera_id** `str` or `int`: `auto` for automatic camera search or manually enter the ID.
- **Obs_capture_fps** `int`: Capture frame rate.

### Aim

- **body_y_offset** `float`: Y-axis offset if the head is not found or head targeting is disabled. For example, `0.35` for upward offset.
![Aim Diagram](https://github.com/SunOner/sunone_aimbot_docs/blob/main/config/media/body_y_offset.png)
- **hideout_targets** `bool`: `true` to enable targeting practice targets, `false` to disable.
- **disable_headshot** `bool`: `true` to disable head targeting, `false` to enable.
- **disable_prediction** `bool`: `true` to disable target position prediction, `false` to enable.
- **prediction_interval** `float`: Target prediction interval.
- **third_person** `bool`: `true` to ignore third-person player, `false` not to ignore.

### Hotkeys

- **hotkey_targeting** `str`: Key for targeting. Supports multiple buttons, e.g., `RightMouseButton,X2MouseButton`.
- **hotkey_exit** `str`: Key to exit the program. Default is `F2`.
- **hotkey_pause** `str`: Key to pause. Default is `F3`.
- **hotkey_reload_config** `str`: Key to reload configuration. Default is `F4`.

### Mouse

- **mouse_dpi** `int`: Software mouse DPI.
- **mouse_sensitivity** `float`: Mouse sensitivity.
- **mouse_fov_width** `int`: Horizontal field of view.
- **mouse_fov_height** `int`: Vertical field of view.
- **mouse_min_speed_multiplier** `float`: Minimum speed multiplier.
- **mouse_max_speed_multiplier** `float`: Maximum speed multiplier.
- **mouse_lock_target** `bool`: `true` to lock target without holding the button, `false` to hold the button.
- **mouse_auto_aim** `bool`: `true` for auto-aim, `false` for manual.

#### Mouse Drivers

- **mouse_ghub** `bool`: Use Logitech GHUB exploit. Requires [GHUB](https://disk.yandex.ru/d/LagJI9dR-kM9cQ).
- **mouse_rzr** `bool`: For Razer mice. Requires [synapse 3](https://www.razer.com/synapse-3).

### Shooting

- **auto_shoot** `bool`: Enable automatic shooting.
- **triggerbot** `bool`: Automatic shooting when targeting.
- **force_click** `bool`: `true` to shoot even outside the aim zone, `false` only within the zone.
- **bScope_multiplier** `float`: Zone multiplier for automatic shooting.

### Arduino

- **arduino_move** `bool`: `true` to send movement commands to Arduino.
- **arduino_shoot** `bool`: `true` to send shooting commands to Arduino.
- **arduino_port** `str`: Arduino COM port (`COM1`, `COM2`, or `auto`).
- **arduino_baudrate** `int`: Data transmission speed.
- **arduino_16_bit_mouse** `bool`: `true` to use 16-bit values for the mouse.

### Artificial Intelligence (AI)

- **AI_model_name** `str`: AI model name.
- **AI_model_image_size** `int`: Image size for the AI model.
- **AI_conf** `float`: AI confidence level for targeting.
- **AI_device** `int` or `str`: Device for computations (`0`, `1`, or `cpu`).
- **AI_enable_AMD** `bool`: `true` to use AMD devices.
- **AI_mouse_net** `bool`: Use neural networks for mouse movement.

### Overlay

- **show_overlay** `bool`: Enable overlay.
- **overlay_show_borders** `bool`: Show overlay borders.
- **overlay_show_boxes** `bool`: Show detected targets.
- **overlay_show_target_line** `bool`: Show lines to the target.
- **overlay_show_target_prediction_line** `bool`: Show prediction line.
- **overlay_show_labels** `bool`: Show target names.
- **overlay_show_conf** `bool`: Show confidence level.

### Debug Window

- **show_window** `bool`: Show debug window.
- **show_detection_speed** `bool`: Show AI processing speed.
- **show_window_fps** `bool`: Show window FPS.
- **show_boxes** `bool`: Show detected objects.
- **show_labels** `bool`: Show object names.
- **show_conf** `bool`: Show confidence level.
- **show_target_line** `bool`: Show line to the target.
- **show_target_prediction_line** `bool`: Show prediction line.
- **show_bScope_box** `bool`: Show auto-shoot zone.
- **show_history_points** `bool`: Show mouse movement history.
- **debug_window_always_on_top** `bool`: Debug window always on top.
- **spawn_window_pos_x** `int`: X coordinate of the debug window.
- **spawn_window_pos_y** `int`: Y coordinate of the debug window.
- **debug_window_scale_percent** `int`: Debug window size in percent.

The debug window name is randomly selected from the `window_names.txt` file.