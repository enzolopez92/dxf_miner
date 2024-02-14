import ezdxf

def main():
    dwg = ezdxf.readfile('/Users/elcaballero/Downloads/CP-JRL-ET-L19-DR-S-03-2026-C01.dxf')

    modelspace = dwg.modelspace()
    for entity in modelspace:
        print(f"Entity type: {entity.dxftype("MTEXT")}")
            #Print or process other attributes of the entity here
            #Example: entity.dxf.layer, entity.dxf.color, entity.dxf.text, etc.

if __name__ == "__main__":
    main()



