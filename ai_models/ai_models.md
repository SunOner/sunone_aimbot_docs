## AI Models
- *.pt: Default AI model.
- *.onnx: The model is optimized to run on processors.
- *.engine: Final exported model, which is faster than the previous two.

## Export .pt model to .engine
> [!NOTE]
> Each model has its own image size with which it was trained, export only with the image size with which it was published.

- Models working directory is `./models` folder.

- Export from Helper:
	- Run helper and go to `EXPORT` tab.
	- Select model.
	- Select image size.
	- Export.
- Export from CMD:
	- All commands are executed in the console window:
	- First, go to the aimbot directory using the command:
	```cmd
	cd C:\Users\your_username\downloads\sunone_aimbot-main
	```
	- Then export the model from the .pt format in .engine format.
	```cmd
	yolo export model="models/sunxds_0.5.6.pt" format=engine device=0 imgsz=640 half=True
	```
	  - `model="model_path/model_name.pt"`: Path to model.
	  - `format=engine`: TensorRT model format.
	  - `half=true`: Use Half-precision floating-point format.
	  - `device=0`: GPU id.
	  - `workspace=8`: (optional) GPU max video memory.
	  - `verbose=False`: (optional) Debug stuff. Convenient function, can show errors when exporting.
- After exporting, the new models will appear in the `./models` folder.