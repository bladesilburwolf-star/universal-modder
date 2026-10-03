# OpenMW Bloodstained: Ritual of the Night Mod

A mod for OpenMW (Morrowind) that adds weapons and enemies from Bloodstained: Ritual of the Night into the world of Morrowind.

## Features

This mod adds:
- **Weapons from Bloodstained**: Iconic weapons like Valmanway (Crissaegrim), Adrasteia (homing gun), and other signature armaments
- **Enemies from Bloodstained**: Demons and creatures from the game, adapted to fit Morrowind's aesthetic
- **New content**: 5 weapons and 5 creatures with placeholder records

## Installation

### Prerequisites
- OpenMW 0.47 or later
- Morrowind game files (Morrowind.esm, Tribunal.esm, Bloodmoon.esm)

### Manual Installation

1. **Copy the mod files** to your OpenMW Data Files directory:
   ```
   cp -r BloodstainedMod/ "$OPENMW_DATA_PATH/Data Files/"
   ```

2. **Or create a separate data folder** and add it to your `openmw.cfg`:
   ```
   data="$HOME/.config/openmw/data/BloodstainedMod"
   ```

3. **Enable the plugin** in OpenMW Launcher:
   - Select "BloodstainedMod.esp" in the Content list
   - Make sure it's loaded AFTER Tribunal and Bloodmoon

4. **Optional**: Add to `openmw.cfg` content line:
   ```
   content=Morrowind.esm
   content=Tribunal.esm
   content=Bloodmoon.esm
   content=BloodstainedMod.esp
   ```

## Mod Structure

```
BloodstainedMod/
├── BloodstainedMod.esp          # Plugin file with records
├── Meshes/
│   └── bloodstained/             # Weapon and creature meshes
│       ├── weapons/
│       │   ├── valmanway.nif
│       │   ├── adrasteia.nif
│       │   ├── enc_orchid.nif
│       │   ├── redbeast.nif
│       │   └── mistilteinn.nif
│       └── creatures/
│           ├── hellhound.nif
│           ├── bloodless.nif
│           ├── gremory.nif
│           ├── alkahest.nif
│           └── andrealphus.nif
└── Textures/
    └── bloodstained/
        ├── weapons/
        └── creatures/
```

## Added Content

### Weapons

| ID | Name | Type | Notes |
|----|------|------|-------|
| `bld_valmanway` | Valmanway | Longsword | Multi-hit, high speed (Crissaegrim equivalent) |
| `bld_adrasteia` | Adrasteia | Marksman | Gun with homing projectiles |
| `bld_enc_orchid` | Encrypted Orchid | Staff | Lightning damage, stun effect |
| `bld_redbeast` | Redbeast's Edge | Battle Axe | High damage, short range |
| `bld_mistilteinn` | Mistilteinn | Staff | Holy damage |

### Enemies

| ID | Name | Level | Notes |
|----|------|-------|-------|
| `bld_hellhound` | Hellhound | 10 | Fire-breathing demonic dog |
| `bld_bloodless` | Bloodless | 10 | Vampire-like creature, drains health |
| `bld_gremory` | Gremory | 25 | Magic-wielding demon |
| `bld_alkahest` | Alkahest | 20 | Poison/acid attacks |
| `bld_andrealphus` | Andrealphus | 30 | Powerful crushing attacks |

## Customization

The ESP file contains placeholder records. To customize:

1. **Edit in OpenMW-CS**:
   - Open `BloodstainedMod.esp` in OpenMW Construction Set
   - Modify weapon stats, creature stats, and other properties
   - Add new records as needed

2. **Add Assets**:
   - Create .nif meshes using Blender with PyNifly plugin
   - Create .dds textures (BC1/BC3/BC7 compression)
   - Place in the appropriate Meshes and Textures directories

3. **Validate**:
   ```bash
   tes3cmd check BloodstainedMod.esp
   ```

## Compatibility

- Compatible with most mods
- Load after major overhauls (Tamriel Rebuilt, etc.)
- May conflict with mods that modify the same leveled lists

## Credits

- Bloodstained: Ritual of the Night - Koei Tecmo Games / ArtPlay
- OpenMW - OpenMW Team
- Weapon and enemy data adapted from Bloodstained Wiki

## Building from Source

If you want to regenerate the plugin file:

```bash
python3 create_bloodstained_esp.py
```

This requires Python 3.6+ (no external dependencies).

## License

This mod is released under the MIT License.

## Changelog

### v1.0.0
- Initial release
- Added 5 Bloodstained weapons
- Added 5 Bloodstained enemies
- Created directory structure for assets
- Added installation instructions
