import sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
import ezdxf

def extract_text_before_font_change(dxf_filename):
    dwg = ezdxf.readfile(dxf_filename)
    modelspace = dwg.modelspace()

    text_values = []
    current_text = ''
    current_font = None

    for entity in modelspace:
        entity_type = entity.dxftype()
        
        if entity_type in ('TEXT', 'MTEXT'):
            font_name = entity.dxf.style  # Style name is the font name
            
            if current_font is None or font_name == current_font:
                text_value = entity.dxf.text
                current_text += text_value + ' '
            else:
                if current_text.strip():  # Append only if there's content
                    text_values.append(current_text.strip())
                current_text = text_value + ' '  # Start new current_text
                current_font = font_name
    
    # Append the last text element
    if current_text.strip():
        text_values.append(current_text.strip())

    return text_values

def main():
    dxf_filename = '/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026-C01.dxf'
    
    text_values = extract_text_before_font_change(dxf_filename)
    for text_value in text_values:
        print(f"Text: {text_value}")

if __name__ == "__main__":
    main()

