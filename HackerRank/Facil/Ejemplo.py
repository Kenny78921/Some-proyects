import xml.etree.ElementTree as ET

tree = ET.parse("nest.xml")
root = tree.getroot()

profundidad = 0
def depth(elem, level):
    global profundidad

    profundidad = max(profundidad, level + 1)  # Update maxdepth to reflect current level (root at 0)

    for child in elem:
        depth(child, level + 1)  # Recur for children, incrementing the level
    return profundidad

depth(root,-1)
print(profundidad)