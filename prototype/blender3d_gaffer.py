# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Satish Goda <satishgoda@live.com>"

import bpy


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the World properties window"""
    bl_label = "World Gaffer"
    bl_idname = "WORLD_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "world"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.label(text="CAMERAS", icon='CAMERA_DATA')
        col.separator()
        
        col = layout.box()
        col_gaffer_cameras = context.view_layer.layer_collection.children['Gaffer'].children['Cameras'].collection
        for camera in col_gaffer_cameras.objects:
            row = col.row()
            row.alignment = 'LEFT'
            if context.active_object == camera:
                row.alert = True
            if not camera in context.selected_objects:
                row.active = False
            if not context.scene.camera == camera:
                op = row.operator('wm.context_set_value', text='scnCam')
                op.data_path = 'scene.camera'
                op.value = "context.scene.view_layers['{0}'].layer_collection.children['Gaffer'].children['Cameras'].collection.objects['{1}']".format(
                                                context.view_layer.name, 
                                                camera.name)
            else:
                row.label(text='                ')

            row.label(text=camera.name)

            row.prop(camera.data, 'clip_start')
            row.prop(camera.data, 'clip_end', )

            row = col.row()
            row.alignment = 'RIGHT'
            row.prop(camera.data.dof, 'use_dof')
            row.prop(camera.data.dof, 'focus_distance')        
            row.prop(camera.data.dof, 'aperture_fstop')
            
            col.separator()
        layout.separator()        


        col = layout.column()
        col.label(text="LIGHTS", icon='LIGHT_DATA')
        col.separator()
        
        col = layout.box()
        col_gaffer = context.view_layer.layer_collection.children['Gaffer'].children['Lights'].collection

        for light in col_gaffer.objects:
            row = col.row()
            if context.active_object == light:
                row.alert = True
            if not light in context.selected_objects:
                row.active = False

            row.label(text=light.name)
            row.prop(light.data, 'type', text='')
            row.prop(light.data, 'color', text='')
            row.prop(light.data, 'energy', text='')
            row.prop(light.data, 'use_shadow', text='')
            row.prop(light, 'hide_viewport', text='')

            row = col.row()
            row.label(text='')

            if isinstance(light.data, bpy.types.AreaLight):
                row.prop(light.data, 'shadow_buffer_clip_start', text='clip')
            else:
                row.label(text='')
            row.prop(light.data, 'shadow_buffer_bias', text='bias')
            
            col.separator()

        layout.separator()
        
        col = layout.column()
        col.alignment = 'LEFT'
        col.label(text="EVEEE SETTIGNS", icon='SCENE')
        col.separator()
    
        col = layout.box()
        row = col.row()
        row.alignment = 'RIGHT'
        col = row.column()
        col.alignment = 'CENTER'
        col.prop(context.scene.eevee, 'use_soft_shadows')  
        col.prop(context.scene.eevee, 'shadow_cube_size')
        col.prop(context.scene.eevee, 'shadow_cascade_size')   
      


def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
