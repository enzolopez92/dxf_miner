import sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
import ezdxf

def find_text_and_dependencies(dxf_filename, target_text):
    dwg = ezdxf.readfile(dxf_filename)

    def find_dependencies(entity):
        dependencies = []

        # Check if the entity has attributes (common for blocks and attributes)
        if entity.dxftype() == 'ATTRIB':
            dependencies.append(f"Attribute: {entity.dxf.tag}")

        # Check if the entity is in a block reference
        if entity.dxftype() == 'INSERT':
            block = entity.block()
            for block_entity in block.modelspace().query('*'):
                dependencies += find_dependencies(block_entity)

        return dependencies

    results = {}

    for entity in dwg.modelspace().query('*'):
        if get_text_from_entity(entity) == target_text:
            dependencies = find_dependencies(entity)
            results[(entity.dxftype(), entity.dxf.handle)] = dependencies

    return results

def get_text_from_entity(entity):
    if entity.dxftype() == 'TEXT':
        return entity.dxf.text
    elif entity.dxftype() == 'MTEXT':
        return entity.plain_text()
    return None

def main():
    dxf_filename = '/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-43-2106-P01.dxf'
    target_text = 'PROJECT NAME'

    result = find_text_and_dependencies(dxf_filename, target_text)

    if result:
        print(f"The text '{target_text}' is located with its dependencies:")
        for (entity_type, entity_handle), dependencies in result.items():
            print(f"Entity Type: {entity_type}")
            print(f"Entity Handle: {entity_handle}")
            if dependencies:
                print("Dependencies:")
                for dep in dependencies:
                    print(f"  {dep}")
    else:
        print(f"The text '{target_text}' was not found in the DXF file.")

if __name__ == "__main__":
    main()

