# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
	"name" : "Segment Changer",
	"author" : "Matthew <makramate12@gmail.com>",
	"version" : (1, 0),
	"blender" : (2, 80, 0),
	"category" : "Mesh",
	"location" : "'N' panel",
	"description" : "Lets you change the number of segments of a cylinder, circle and sphere even after moving it",
}

import bpy

from .segment_changer_op 	import MESH_OT_segment_changer
from .segment_changer_panel import VIEW3D_PT_segment_changer

def register():
	bpy.types.Object.segments = bpy.props.IntProperty(
		name = 'Number of Segments',
		min = 3,
		soft_max = 500,
		default=32,
	)

	bpy.types.Object.rings = bpy.props.IntProperty(
		name = 'Number of Rings',
		min = 3,
		soft_max = 500,
		default=16,
	)

	bpy.utils.register_class(MESH_OT_segment_changer)
	bpy.utils.register_class(VIEW3D_PT_segment_changer)

def unregister():
	bpy.utils.unregister_class(MESH_OT_segment_changer)
	bpy.utils.unregister_class(VIEW3D_PT_segment_changer)