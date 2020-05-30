import bpy

class VIEW3D_PT_segment_changer(bpy.types.Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = "Segment"
	bl_label = "Segment Changer"

	def draw(self, context):
		if context.object and "Cylinder" in context.active_object.name:
			col = self.layout.column(align=True)
			col.prop(context.object, 'segments')
			col = self.layout.column(align=True)
			col.operator('mesh.segment_changer', text='Apply Segments')
		elif context.object and "Sphere" in context.active_object.name:
			col = self.layout.column(align=True)
			col.prop(context.object, 'segments')
			col.prop(context.object, 'rings')
			col = self.layout.column(align=True)
			col.operator('mesh.segment_changer', text='Apply Segments')
		elif context.object and "Circle" in context.active_object.name:
			col = self.layout.column(align=True)
			col.prop(context.object, 'segments', text='Number of Vertices')
			col = self.layout.column(align=True)
			col.operator('mesh.segment_changer', text='Apply Segments')
		else:
			col = self.layout.column(align=True)
			col.label(text='Select an unmodified')
			col.label(text='Cylinder')
			col.label(text='Sphere')
			col.label(text='Circle')