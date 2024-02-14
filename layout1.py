import ezdxf





def extract_text_from_entity(entity):
    text = None
    if 'TEXT' in entity.dxftype() or 'MTEXT' in entity.dxftype() or 'U5' in entity.dxftype() or 'ATTDEF' in entity.dxftype():
        text = entity.dxf.text
    elif 'ATTRIB' in entity.dxftype() or 'ATTDEF' in entity.dxftype():
        text = entity.dxf.text

    return text

def main():
    dxf_filename = '/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026-C01.dxf'
    layout_name = 'CP-JRL-ET-L19-DR-S-03-2026-C01'  # Replace with the actual layout name

    dwg = ezdxf.readfile(dxf_filename)

    if layout_name in dwg.layouts:
        layout = dwg.layouts.get(layout_name)
        
        for entity in layout:
            text_value = extract_text_from_entity(entity)
            if text_value:
                print(f"Text: {text_value}")
            
    else:
       # print(f"Layout '{layout_name}' not found.")
       print(f"Layout '{layout_name}' not found.")

if __name__ == "__main__":
    main()