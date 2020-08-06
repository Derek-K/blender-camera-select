# blender-camera-select
## Simple python script to select which camera view to render with blender headless mode
  
Use this script to specify which camera to use for render while running blender in headless (a.k.a. CLI) mode.  
  
Example usage:  
`blender -noaudio -b {blender file} -P cameraselect.py -o // -s {start frame} -e {end frame} -a -- {camera name}`

Where:  
- blender file - .blend file
- cameraselect.py - this script
- start/end frame - for animation
- camera name - the name of the camera, use double quote if it contain spaces (e.g. "My Special Camera")

For more details on blender CLI parameters please check with blender project documents.
