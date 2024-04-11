import bpy
import math
import pathlib

# Clear the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#Take image paths [] and import image 
def import_image_as_planes(image_paths):
    for image_path in image_paths:
        bpy.ops.import_image.to_plane(files=[{"name": str(image_path)}], directory= str(image_path.parent))
 
#Adjust the scale       
def correct_scale_of_planes(scale):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.transform.resize(value=(scale,scale,scale))
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
       
        
#Add new camera
new_camera_data = bpy.data.cameras.new(name="camera")
new_camera_data.lens = 85
new_camera_data.sensor_width = 18.96
new_camera_data.sensor_height = 10

middle_camera = bpy.data.objects.new("Camera", new_camera_data)
bpy.context.scene.collection.objects.link (middle_camera)

middle_camera.location = (0,-90,0)
middle_camera.rotation_euler[0]= math.radians(90)


bpy.context.scene.camera = middle_camera

new_camera_data2 = bpy.data.cameras.new(name="camera")
new_camera_data2.lens = 85
new_camera_data2.sensor_width = 18.96
new_camera_data2.sensor_height = 10

left_camera = bpy.data.objects.new("Camera", new_camera_data2)
bpy.context.scene.collection.objects.link (left_camera)

left_camera.location = (-45,-90,0)
left_camera.rotation_euler[0]= math.radians(88)
left_camera.rotation_euler[1]= math.radians(-8)
left_camera.rotation_euler[2]= math.radians(-25)

bpy.context.scene.camera = left_camera

new_camera_data3 = bpy.data.cameras.new(name="camera")
new_camera_data3.lens = 85
new_camera_data3.sensor_width = 18.96
new_camera_data3.sensor_height = 10

right_camera = bpy.data.objects.new("Camera", new_camera_data3)
bpy.context.scene.collection.objects.link (right_camera)

right_camera.location = (45,-90,0)
right_camera.rotation_euler[0]= math.radians(-89)
right_camera.rotation_euler[1]= math.radians(183)
right_camera.rotation_euler[2]= math.radians(-154)

bpy.context.scene.camera = right_camera



if __name__ == "__main__":
    image_paths = [
        pathlib.Path.home() / "Documents" / "C01020_Env.png",
    ]
    import_image_as_planes(image_paths)
    scale= 25
    correct_scale_of_planes(scale)