#!/usr/bin/env python3
"""
Create a minimal OpenMW ESP plugin for Bloodstained: Ritual of the Night content.

This creates a basic ESP file structure that can be loaded by OpenMW.
The ESP contains placeholder records that can be edited in OpenMW-CS.

For a fully functional mod, you should:
1. Run this script to create the basic structure
2. Open the ESP in OpenMW-CS
3. Add proper weapon and creature records
4. Add meshes and textures
5. Validate with tes3cmd
"""

import struct
from pathlib import Path


def create_minimal_esp():
    """Create a minimal valid ESP file for OpenMW."""
    
    buffer = bytearray()
    
    # File header
    buffer.extend(b'TES3')  # File ID
    buffer.extend(struct.pack('<I', 12))  # Header size
    buffer.extend(struct.pack('<f', 1.3))  # Version (Morrowind)
    buffer.extend(struct.pack('<I', 0))  # File type flags (0 = ESP, 1 = ESM)
    
    # TES3 record (plugin header)
    record_start = len(buffer)
    buffer.extend(b'TES3')  # Record type
    buffer.extend(b'\x00\x00\x00\x00')  # Size placeholder
    
    # HEDR subrecord (12 bytes: version float + file type int)
    buffer.extend(b'HEDR')
    hedr_data = struct.pack('<fI', 1.3, 0)  # Version and flags
    buffer.extend(struct.pack('<H', len(hedr_data)))
    buffer.extend(hedr_data)
    
    # CNAM subrecord (Author)
    author = b'Vibe Code\x00'
    buffer.extend(b'CNAM')
    buffer.extend(struct.pack('<H', len(author)))
    buffer.extend(author)
    
    # SNAM subrecord (Description)
    desc = b'Bloodstained: Ritual of the Night weapons and enemies\x00'
    buffer.extend(b'SNAM')
    buffer.extend(struct.pack('<H', len(desc)))
    buffer.extend(desc)
    
    # MAST subrecord (Master file - Morrowind.esm)
    master = b'Morrowind.esm\x00'
    buffer.extend(b'MAST')
    buffer.extend(struct.pack('<H', len(master)))
    buffer.extend(master)
    
    # Update TES3 record size
    record_size = len(buffer) - record_start - 4
    buffer[record_start+4:record_start+8] = struct.pack('<I', record_size)
    
    # Now add weapon records with minimal data
    weapons = [
        ('bld_valmanway', 'Valmanway', 'meshes\\bloodstained\\weapons\\valmanway.nif'),
        ('bld_adrasteia', 'Adrasteia', 'meshes\\bloodstained\\weapons\\adrasteia.nif'),
        ('bld_enc_orchid', 'Encrypted Orchid', 'meshes\\bloodstained\\weapons\\enc_orchid.nif'),
        ('bld_redbeast', 'Redbeast Edge', 'meshes\\bloodstained\\weapons\\redbeast.nif'),
        ('bld_mistilteinn', 'Mistilteinn', 'meshes\\bloodstained\\weapons\\mistilteinn.nif'),
    ]
    
    for editor_id, full_name, model_path in weapons:
        record_start = len(buffer)
        buffer.extend(b'WEAP')
        buffer.extend(b'\x00\x00\x00\x00')  # Size placeholder
        
        # NAME
        name_data = editor_id.encode('utf-8') + b'\x00'
        buffer.extend(b'NAME')
        buffer.extend(struct.pack('<H', len(name_data)))
        buffer.extend(name_data)
        
        # MODL
        model_data = model_path.encode('utf-8') + b'\x00'
        buffer.extend(b'MODL')
        buffer.extend(struct.pack('<H', len(model_data)))
        buffer.extend(model_data)
        
        # FNAM
        fullname_data = full_name.encode('utf-8') + b'\x00'
        buffer.extend(b'FNAM')
        buffer.extend(struct.pack('<H', len(fullname_data)))
        buffer.extend(fullname_data)
        
        # WPDT - Weapon data (26 bytes for TES3)
        # Format: type(i32), speed(f32), reach(f32), value(i32), 
        #         health(i32), weight(f32), damage(i16)
        wpdt = struct.pack('<i f f i i f h',
                           1, 1.5, 1.0,  # type=1 (longsword), speed, reach
                           100, 100, 5.0, 15)  # value, health, weight, damage
        buffer.extend(b'WPDT')
        buffer.extend(struct.pack('<H', len(wpdt)))
        buffer.extend(wpdt)
        
        # Update record size
        record_size = len(buffer) - record_start - 4
        buffer[record_start+4:record_start+8] = struct.pack('<I', record_size)
    
    # Add creature records
    creatures = [
        ('bld_hellhound', 'Hellhound', 'meshes\\bloodstained\\creatures\\hellhound.nif'),
        ('bld_bloodless', 'Bloodless', 'meshes\\bloodstained\\creatures\\bloodless.nif'),
        ('bld_gremory', 'Gremory', 'meshes\\bloodstained\\creatures\\gremory.nif'),
        ('bld_alkahest', 'Alkahest', 'meshes\\bloodstained\\creatures\\alkahest.nif'),
        ('bld_andrealphus', 'Andrealphus', 'meshes\\bloodstained\\creatures\\andrealphus.nif'),
    ]
    
    for editor_id, full_name, model_path in creatures:
        record_start = len(buffer)
        buffer.extend(b'CREA')
        buffer.extend(b'\x00\x00\x00\x00')  # Size placeholder
        
        # NAME
        name_data = editor_id.encode('utf-8') + b'\x00'
        buffer.extend(b'NAME')
        buffer.extend(struct.pack('<H', len(name_data)))
        buffer.extend(name_data)
        
        # MODL
        model_data = model_path.encode('utf-8') + b'\x00'
        buffer.extend(b'MODL')
        buffer.extend(struct.pack('<H', len(model_data)))
        buffer.extend(model_data)
        
        # FNAM
        fullname_data = full_name.encode('utf-8') + b'\x00'
        buffer.extend(b'FNAM')
        buffer.extend(struct.pack('<H', len(fullname_data)))
        buffer.extend(fullname_data)
        
        # DATA - Creature stats (44 bytes for TES3)
        # Format: health(i32), magicka(i32), fatigue(i32),
        #         soul(i16), combat(i16), magic(i16), stealth(i16),
        #         strength(i16), intelligence(i16), willpower(i16), agility(i16),
        #         speed(i16), endurance(i16), personality(i16), luck(i16),
        #         level(i32), unknown(i32)
        data = struct.pack('<i i i h h h h h h h h h h h h i i',
                           100, 50, 100,  # health, magicka, fatigue
                           0, 0, 0, 0,  # soul, combat, magic, stealth
                           30, 30, 30, 30,  # strength, intelligence, willpower, agility
                           30, 30, 30, 30,  # speed, endurance, personality, luck
                           10, 0)  # level, unknown
        buffer.extend(b'DATA')
        buffer.extend(struct.pack('<H', len(data)))
        buffer.extend(data)
        
        # Update record size
        record_size = len(buffer) - record_start - 4
        buffer[record_start+4:record_start+8] = struct.pack('<I', record_size)
    
    return buffer


def main():
    output_dir = Path(__file__).parent / 'BloodstainedMod'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / 'BloodstainedMod.esp'
    
    print(f"Creating BloodstainedMod.esp at {output_path}")
    
    esp_data = create_minimal_esp()
    
    with open(output_path, 'wb') as f:
        f.write(esp_data)
    
    print(f"ESP file created: {len(esp_data)} bytes")
    
    # Create directory structure
    meshes_weapons = output_dir / 'Meshes' / 'bloodstained' / 'weapons'
    meshes_creatures = output_dir / 'Meshes' / 'bloodstained' / 'creatures'
    textures_weapons = output_dir / 'Textures' / 'bloodstained' / 'weapons'
    textures_creatures = output_dir / 'Textures' / 'bloodstained' / 'creatures'
    
    meshes_weapons.mkdir(parents=True, exist_ok=True)
    meshes_creatures.mkdir(parents=True, exist_ok=True)
    textures_weapons.mkdir(parents=True, exist_ok=True)
    textures_creatures.mkdir(parents=True, exist_ok=True)
    
    # Create README files
    with open(meshes_weapons / 'README.txt', 'w') as f:
        f.write("Place .nif weapon meshes here:\n\n")
        f.write("- valmanway.nif\n")
        f.write("- adrasteia.nif\n")
        f.write("- enc_orchid.nif\n")
        f.write("- redbeast.nif\n")
        f.write("- mistilteinn.nif\n")
    
    with open(meshes_creatures / 'README.txt', 'w') as f:
        f.write("Place .nif creature meshes here:\n\n")
        f.write("- hellhound.nif\n")
        f.write("- bloodless.nif\n")
        f.write("- gremory.nif\n")
        f.write("- alkahest.nif\n")
        f.write("- andrealphus.nif\n")
    
    print("Directory structure created")
    print(f"\nMod files in: {output_dir.absolute()}")
    print("\nNEXT STEPS:")
    print("1. Open BloodstainedMod.esp in OpenMW-CS")
    print("2. Edit weapon and creature records with proper stats")
    print("3. Add meshes (.nif) and textures (.dds)")
    print("4. Validate with: tes3cmd check BloodstainedMod.esp")
    print("5. Enable in OpenMW Launcher")


if __name__ == '__main__':
    main()
