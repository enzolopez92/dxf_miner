import sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
import ezdxf





def find_string_in_dxf(dxf_file_path, search_string):
    try:
        with open(dxf_file_path, 'r') as dxf_file:
            file_contents = dxf_file.read()
            if search_string in file_contents:
                print(f"Found '{search_string}' in the DXF file.")
            else:
                print(f"'{search_string}' not found in the DXF file.")
    except FileNotFoundError:
        print(f"DXF file not found: {dxf_file_path}")

if __name__ == "__main__":
    dxf_file_path = "/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026.dxf"
    search_string = "PROJECT NAME"
    
    find_string_in_dxf(dxf_file_path, search_string)


import ezdxf

def find_text_and_dependencies(dxf_file_path, search_string):
    doc = ezdxf.readfile(dxf_file_path)
    msp = doc.modelspace()
    
    found_entities = []
    
    for entity in msp:
        if entity.dxftype() == 'TEXT' and search_string in entity.dxf.text:
            found_entities.append(entity)
    
    if found_entities:
        print(f"Found '{search_string}' in the following entities:")
        for entity in found_entities:
            print(f"Entity Type: {entity.dxftype()}, Layer: {entity.dxf.layer}, Text: {entity.dxf.text}")
            
            # Check if the text is part of an attributed block
            if entity.get_layout() is not None:
                print(f"Belongs to Block: {entity.get_layout().name}")

    else:
        print(f"'{search_string}' not found in the DXF file.")

if __name__ == "__main__":
    dxf_file_path = "/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026.dxf"
    search_string = "PROJECT NAME"
    
    find_text_and_dependencies(dxf_file_path, search_string)

