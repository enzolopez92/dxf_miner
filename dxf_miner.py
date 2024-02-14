import sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
import ezdxf

def main():
   dwg = ezdxf.readfile('/home/ubuntu/Downloads/CP-JRL-ET-L19-DR-S-03-2026.dxf')

   modelspace = dwg.modelspace()
   for entity in modelspace:
       entity_type = entity.dxftype()  # Get the entity type
        
       if entity_type in ["TEXT", "LABEL"]:
           text_value = entity.dxf.text  # Get the text content from TEXT or LABEL entity
           print(f"Text: {text_value}")
        
       # You can add more conditions here for different entity types

if __name__ == "__main__":
   main()








# import sys
# sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
# import ezdxf

# def main():
#    dwg = ezdxf.readfile('/home/ubuntu/Downloads/CP-JRL-ET-L19-DR-S-03-2026.dxf')

#    modelspace = dwg.modelspace()
#    for entity in modelspace:
#        entity_type = entity.dxftype()  # Get the entity type
        
#        if entity_type == 'TEXT':
#            text_value = entity.dxf.text
#            print(f"Text: {text_value}")
        
#        elif entity_type == 'CIRCLE':
#            radius = entity.dxf.radius
#            center = entity.dxf.center
#            print(f"Circle - Radius: {radius}, Center: {center}")
        
#         #Add more conditions for other entity types
        
#        elif entity_type == 'LINE':
#            pass  # Skip processing LINE entities
#        elif entity_type == 'POINT':
#            pass  # Skip processing LINE entities
#        elif entity_type == 'INSERT':
#            pass  # Skip processing LINE entities
        
#        else:
#            print(f"Unhandled entity type: {entity_type}")

# if __name__ == "__main__":
#     main()






# import sys
# sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
# import ezdxf

# def extract_text_before_font_change(dxf_filename):
#     dwg = ezdxf.readfile(dxf_filename)
#     modelspace = dwg.modelspace()

#     text_values = []
#     current_text = ''
#     current_font = None

#     for entity in modelspace:
#         entity_type = entity.dxftype()
        
#         if entity_type in ('TEXT', 'MTEXT'):
#             font_name = entity.dxf.style  # Style name is the font name
            
#             if current_font is None or font_name == current_font:
#                 text_value = entity.dxf.text
#                 current_text += text_value + ' '
#             else:
#                 if current_text.strip():  # Append only if there's content
#                     text_values.append(current_text.strip())
#                 current_text = text_value + ' '  # Start new current_text
#                 current_font = font_name
    
#     # Append the last text element
#     if current_text.strip():
#         text_values.append(current_text.strip())

#     return text_values

# def main():
#     dxf_filename = '/home/ubuntu/Downloads/CP-JRL-ET-L19-DR-S-03-2026.dxf'
    
#     text_values = extract_text_before_font_change(dxf_filename)
#     for text_value in text_values:
#         print(f"Text: {text_value}")

# if __name__ == "__main__":
#     main()