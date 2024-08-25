# Helper - Installation Assistant for All Components
1. Python 3.11.6 is required for automatic installation. [Download Python](https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe).
   - Make sure to check the `Add Python 3.11.6 to PATH` box before installation.
![](https://github.com/SunOner/sunone_aimbot_docs/blob/main/install/media/python_add_to_path.png)
2. Download the repository and extract it, for example, to your desktop. [Download](https://github.com/SunOner/sunone_aimbot/archive/refs/heads/main.zip).
3. Navigate to the folder you extracted and run `run_helper.bat`.
4. The script will first check the installed components necessary for the update.
5. Next, you will see buttons in the menu. First, download and install CUDA, Torch then TensorRT.
6. Without exiting the program, you can check functionality using the `Test detections` button.
7. Export the AI model to the `.engine` format to improve performance. [See AI MODELS Docs](https://github.com/SunOner/sunone_aimbot_docs/blob/main/ai_models/ai_models.md).
8. Everything should be ready. Run run_ai.bat or type `py run.py` in cmd.
- All issues and errors can be found on the official [Discord server](https://discord.gg/sunone).