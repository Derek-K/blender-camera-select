import sys
import bpy

#
# Usage:
# blender -noaudio -b scene.blend -P cameraselect.py -o // -s 001 -e 001 -a -- "My Camera"
#
# - https://github.com/Derek-K/blender-camera-select
   
camVar = sys.argv[-1]
bpy.context.scene.camera = bpy.data.objects[camVar]
