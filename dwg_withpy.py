import ezdxf 

dwg = ezdxf.readfile('/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026-C01.dwg') 

modelspace = dwg.modelspace() 
for entity in modelspace: 
    # Extract data from the entity 
    # # Example: entity.dxf.layer, entity.dxf.color, entity.dxf.text, etc
    # 
        print(f"Entity type: {entity.dxftype()}")
        # Print or process other attributes of the entity here
        # Example: entity.dxf.layer, entity.dxf.color, entity.dxf.text, etc.

if __name__ == "__main__":
    main() 
