from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend

width = 960
height = 540

rend = Renderer(width, height)

rend.dirLight = V3(1,0,0)

#Medium Shot
rend.glViewMatrix(translate = V3(-3,5,0),
                  rotate = V3(0,10,0))
#Low Angle
#rend.glViewMatrix(translate = V3(-3,5,0),
#                  rotate = V3(-30,-45,10))
#High Angle
#rend.glViewMatrix(translate = V3(-3,5,0),
#                  rotate = V3(60,-45,0))
#Dutch Angle
#rend.glViewMatrix(translate = V3(-8,5,4),
#                  rotate = V3(30,10,60))


rend.active_texture = Texture("models/model.bmp")
rend.active_shader = flat
rend.glLoadModel("models/face.obj",
                 translate = V3(-4, 0, -10),
                 scale = V3(3,3,3),
                 rotate = V3(0,0,0))

rend.glFinish("output.bmp")
