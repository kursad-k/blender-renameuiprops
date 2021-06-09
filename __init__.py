bl_info = {
    "name": "Rename UI Properties",
    "author": "Kursad Karatas",
    "version": (0, 1),
    "blender": (2, 93, 0),
    "description": "Renames the active ui property",
    "warning": "",
    "doc_url": "",
    "category": "Generic",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty,StringProperty


def rename_vertex_group(self, context):
  
 context.object.vertex_groups.active.name=self.vgrpname

class OBJECT_OT_RenameVertexGroup(Operator):
    """Rename the active vertex group"""
    bl_idname = "object.renamevertexgroup"
    bl_label = "Rename the current vertex group"
    bl_options = {'REGISTER', 'UNDO'}

    vgrpname: StringProperty(name="vgrpname",default="")

    def execute(self, context):
        rename_vertex_group(self, context)

        return {'FINISHED'}


    def invoke(self, context, event):
       
        wm = context.window_manager
        self.vgrpname=context.object.vertex_groups.active.name

        return wm.invoke_props_dialog( self )



def menu_draw(self, context):
    self.layout.separator()

    self.layout.operator(OBJECT_OT_RenameVertexGroup.bl_idname,text="Rename")

def register():
    bpy.utils.register_class(OBJECT_OT_RenameVertexGroup)
    bpy.types.MESH_MT_vertex_group_context_menu.append(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_RenameVertexGroup)
    bpy.types.MESH_MT_vertex_group_context_menu.remove(menu_draw)


if __name__ == "__main__":
    register()
