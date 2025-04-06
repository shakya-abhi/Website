import pythreejs as three
from IPython.display import display
import numpy as np

# Create the scene
scene = three.Scene()

# Create the camera
camera = three.PerspectiveCamera(position=[3, 3, 3], lookAt=[0, 0, 0])

# Create the lighting
light = three.AmbientLight(color='white', intensity=1)
scene.add(light)

# Function to create a body part
def create_part(geometry, material, position):
    part = three.Mesh(geometry=geometry, material=material)
    part.position = position
    return part

# Body (cylinder for simplification)
body_geometry = three.CylinderGeometry(radiusTop=0.5, radiusBottom=0.7, height=2)
body_material = three.MeshLambertMaterial(color='lightblue')
body = create_part(body_geometry, body_material, position=[0, 0, 0])

# Head (sphere for simplicity)
head_geometry = three.SphereGeometry(radius=0.8, widthSegments=32, heightSegments=16)
head_material = three.MeshLambertMaterial(color='peachpuff')
head = create_part(head_geometry, head_material, position=[0, 1.5, 0])

# Arms (cylinders)
arm_geometry = three.CylinderGeometry(radiusTop=0.1, radiusBottom=0.1, height=2)
arm_material = three.MeshLambertMaterial(color='lightblue')
left_arm = create_part(arm_geometry, arm_material, position=[-1, 0.5, 0])
right_arm = create_part(arm_geometry, arm_material, position=[1, 0.5, 0])

# Legs (cylinders)
leg_geometry = three.CylinderGeometry(radiusTop=0.15, radiusBottom=0.15, height=2)
leg_material = three.MeshLambertMaterial(color='lightblue')
left_leg = create_part(leg_geometry, leg_material, position=[-0.5, -1.5, 0])
right_leg = create_part(leg_geometry, leg_material, position=[0.5, -1.5, 0])

# Adding all parts to the scene
scene.add(body)
scene.add(head)
scene.add(left_arm)
scene.add(right_arm)
scene.add(left_leg)
scene.add(right_leg)

# Create the renderer
renderer = three.WebGLRenderer(camera=camera, scene=scene, width=800, height=600)

# Display the character
display(renderer)
