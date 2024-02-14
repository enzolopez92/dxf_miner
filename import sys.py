import sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
import ezdxf

def main():
   dwg = ezdxf.readfile('/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026-C01.dxf')

   modelspace = dwg.modelspace()
   for entity in modelspace:
       entity_type = entity.dxftype()  # Get the entity type
        
       if entity_type == 'TEXT':
           text_value = entity.dxf.text
           print(f"Text: {text_value}")
        
       elif entity_type == 'CIRCLE':
           radius = entity.dxf.radius
           center = entity.dxf.center
           print(f"Circle - Radius: {radius}, Center: {center}")
        
        Add more conditions for other entity types
        
       elif entity_type == 'LINE':
           pass  # Skip processing LINE entities
       elif entity_type == 'POINT':
           pass  # Skip processing LINE entities
       elif entity_type == 'INSERT':
           pass  # Skip processing LINE entities
        
       else:
           print(f"Unhandled entity type: {entity_type}")

if __name__ == "__main__":
    main()


