import cv2
import bpy
import bpycv
import random
import numpy as np
import os

print(os.getcwd())
print('aaaaaaaaaaaaaaaaaaaaaa')

# # remove all MESH objects
# [bpy.data.objects.remove(obj) for obj in bpy.data.objects if obj.type == "MESH"]

# for index in range(1, 20):
#     # create cube and sphere as instance at random location
#     location = [random.uniform(-2, 2) for _ in range(3)]
#     if index % 2:
#         bpy.ops.mesh.primitive_cube_add(size=0.5, location=location)
#         categories_id = 1
#     else:
#         bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=location)
#         categories_id = 2
# obj = bpy.context.active_object
#     # set each instance a unique inst_id, which is used to generate instance annotation.
# obj["inst_id"] = categories_id * 1000 + index


# obj = bpy.data.objects['S-IV b']
# obj["inst_id"] = 1
# obj = bpy.data.objects['land_ocean_ice_cloud_8192']
# obj["inst_id"] = 0

# obj = bpy.data.objects['S-IV b']
# obj["inst_id"] = 1000

# def my_activator(obj_name):
#     # 全てのオブジェクトのリスト bpy.data.objects のうち obj_name を持つオブジェクトをアクティブ化
#     bpy.context.scene.objects.active = bpy.data.objects[obj_name]

# my_activator('S-IV b')


bpy.data.objects["land_ocean_ice_cloud_8192"].hide_render = False
# render image, instance annoatation and depth in one line code
result = bpycv.render_data()
# result["ycb_meta"] is 6d pose GT

print(result["image"].shape)

number = 8

# save result
cv2.imwrite(
    "C://train//input//" + str(number) + ".jpg", result["image"][..., ::-1]
)  # transfer RGB image to opencv's BGR

# # save instance map as 16 bit png
# np.save("demo-inst.npy", result["inst"])  # save as numpy array
# cv2.imwrite("C:/demo-inst.png", np.uint16(result["inst"]))
# # the value of each pixel represents the inst_id of the object

# convert depth units from meters to millimeters
# depth_in_mm = result["depth"] * 1000
# cv2.imwrite("C:/demo-depth.png", np.uint8(depth_in_mm))  # save as 16bit png

# # visualization instance mask, RGB, depth for human
# cv2.imwrite("C:/demo-vis(inst_rgb_depth).jpg", result.vis()[..., ::-1])






bpy.data.objects["land_ocean_ice_cloud_8192"].hide_render = True

result = bpycv.render_data()
# result["ycb_meta"] is 6d pose GT

print(result["image"].shape)

# # save result
# cv2.imwrite(
#     "C:/demo-rgb.jpg", result["image"][..., ::-1]
# )  # transfer RGB image to opencv's BGR

# convert depth units from meters to millimeters
depth_in_mm = result["depth"] * 1000
cv2.imwrite("C://train//output//" + str(number) + ".jpg", np.uint16(depth_in_mm))  # save as 16bit png