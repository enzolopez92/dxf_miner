import sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
import ezdxf

def find_text_in_block(block, target_text):
    for entity in block:
        if entity.dxftype() == 'TEXT' or entity.dxftype() == 'MTEXT':
            if entity.dxf.text == target_text:
                return entity
    return None

def find_text_in_layout(layout, target_text, block_name):
    for entity in layout:
        if entity.dxftype() == 'INSERT' and entity.dxf.name == block_name:
            block = entity.block()
            found_text = find_text_in_block(block, target_text)
            if found_text:
                return found_text
    return None

def main():
    dxf_filename = '/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026-C01.dxf'
    target_text = 'PROJECT NAME'
    block_name = 'JRL_TITLE BLOCK'  # Specify the block name

    dwg = ezdxf.readfile(dxf_filename)
    
    for layout in dwg.layouts:
        found_text_entity = find_text_in_layout(layout, target_text, block_name)
        if found_text_entity:
            print(f"The text '{target_text}' is located in layout '{layout.name}'.")
            break  # If found, exit the loop
    else:
        print(f"The text '{target_text}' was not found in any layout or block '{block_name}'.")

if __name__ == "__main__":
    main()

