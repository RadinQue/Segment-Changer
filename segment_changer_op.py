import bpy

###
# Disclaimer: I literally have no idea what am I doing.
# I do C++ not Python :c
###

class MESH_OT_segment_changer(bpy.types.Operator):
	"""Changes the number of segments of the selected cylinder"""
	bl_idname = "mesh.segment_changer"
	bl_label = "Change Segments"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		loc_x = context.active_object.location[0]
		loc_y = context.active_object.location[1]
		loc_z = context.active_object.location[2]

		rot_x = context.active_object.rotation_euler[0]
		rot_y = context.active_object.rotation_euler[1]
		rot_z = context.active_object.rotation_euler[2]

		scale_x = context.active_object.scale[0]
		scale_y = context.active_object.scale[1]
		scale_z = context.active_object.scale[2]

		original_dim_x = context.active_object.dimensions[0]
		original_dim_y = context.active_object.dimensions[1]
		original_dim_z = context.active_object.dimensions[2]

		segments = context.active_object.segments
		if "Cylinder" in context.active_object.name:
			bpy.ops.object.delete(use_global=False)
			bpy.ops.mesh.primitive_cylinder_add(vertices=segments, align='WORLD', location=(loc_x, loc_y, loc_z), rotation=(rot_x, rot_y, rot_z), scale=(1, 1, 1))
		elif "Circle" in context.active_object.name:
			bpy.ops.object.delete(use_global=False)
			bpy.ops.mesh.primitive_circle_add(vertices=segments, align='WORLD', location=(loc_x, loc_y, loc_z), rotation=(rot_x, rot_y, rot_z), scale=(1, 1, 1))
		elif "Sphere" in context.active_object.name:
			rings = context.active_object.rings
			bpy.ops.object.delete(use_global=False)
			bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, align='WORLD', location=(loc_x, loc_y, loc_z), rotation=(rot_x, rot_y, rot_z), scale=(1, 1, 1))

		context.active_object.dimensions[0] = original_dim_x
		context.active_object.dimensions[1] = original_dim_y
		context.active_object.dimensions[2] = original_dim_z

		context.active_object.scale[0] = scale_x
		context.active_object.scale[1] = scale_y
		context.active_object.scale[2] = scale_z

		return {'FINISHED'}
