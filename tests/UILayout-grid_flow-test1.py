import bpy


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Scene Gaffer"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "world"

    def draw(self, context):
        layout = self.layout

        lights = context.view_layer.layer_collection.children['Gaffer'].children['Lights'].collection.objects

        gf = layout.grid_flow(row_major=True, columns=4, even_columns=not True, align=not True)
        gf.scale_y = 1.0
        gf.alignment = 'LEFT'

        gf.label(text='')
        gf.label(text='')
        gf.label(text='')
        gf.label(text='')

        for light in lights:
            gf.prop(light, 'hide_viewport', text='')
            gf.label(text=light.name)
            gf.prop(light.data, 'type', text='')
            gf.prop(light.data, 'color', text='')
            
            gf.label(text='')
            gf.label(text='')

            wtf = gf.box()
            wtf.prop(light.data, 'energy')
            wtf.prop(light.data, 'specular_factor')
            if isinstance(light.data, (bpy.types.PointLight, bpy.types.SpotLight)):
                wtf.prop(light.data, 'shadow_soft_size')
            elif isinstance(light.data, bpy.types.AreaLight):
                wtf.prop(light.data, 'shape')
                wtf.prop(light.data, 'size')
                if light.data.shape in ('RECTANGLE', 'ELLIPSE'):
                    wtf.prop(light.data, 'size_y')
            elif isinstance(light.data, bpy.types.SunLight):
                wtf.prop(light.data, 'angle')
            
            wtf = gf.box()
            wtf.scale_y = 1.1
            wtf.prop(light.data, 'use_shadow', text='Toggle Shadows')
            wtf.prop(light.data, 'use_contact_shadow', text='Toggle Contact Shadows')
            if not isinstance(light.data, bpy.types.SunLight):
                wtf.prop(light.data, 'shadow_buffer_clip_start')
            wtf.prop(light.data, 'shadow_buffer_bias', text='bias')

def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
