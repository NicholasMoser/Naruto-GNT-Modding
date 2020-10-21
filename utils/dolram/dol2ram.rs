use std::env;

// The sections of the GNT4 dol, with the exception of bss, sbss, and sbss2 since they aren't in the dol.
enum Section {
    INIT,
    TEXT,
    CTORS,
    DTORS,
    RODATA,
    DATA,
    SDATA,
    SDATA2
}

// Takes in a dol offset hex String, such as 26F0 and returns the section and ram address
// correlated with it. Do not include 0x before the hex String.
//
// # Example
//
// ```bash
// dol2ram 26F0
// ```
//
fn main() {
    
    let arguments: Vec<String> = env::args().collect();
    if arguments.len() == 1 {
        println!("Please include dol offset hex string argument.")
    } else if arguments.len() > 2 {
        println!("Please provide exactly one argument.")
    } else {
        let dol_offset = i64::from_str_radix(&arguments[1], 16).unwrap();
        let section = get_section(dol_offset);
        let add_amount = get_add_amount(section);
        let ram_address = dol_offset + add_amount;
        println!("Offset:  {:X}", ram_address);
    }
}

// Get the amount to add to the offset to get the ram address. This depends on which
// section is referenced since some sections in the dol are skipped but are present in ram.
fn get_add_amount(section: Section) -> i64 {
  match section {
    Section::INIT => {
      println!("Section: INIT");
      return 0x80003000;
    },
    Section::TEXT => {
      println!("Section: TEXT");
      return 0x80003000;
    },
    Section::CTORS => {
      println!("Section: CTORS");
      return 0x80003000;
    },
    Section::DTORS => {
      println!("Section: DTORS");
      return 0x80003000;
    },
    Section::RODATA => {
      println!("Section: RODATA");
      return 0x80003000;
    },
    Section::DATA => {
      println!("Section: DATA");
      return 0x80003000;
    },
    Section::SDATA => {
      println!("Section: SDATA");
      return 0x80056F40;
    },
    Section::SDATA2 => {
      println!("Section: SDATA2");
      return 0x80057C00;
    }
  };
}

// Get the section associated with this ram address.
fn get_section(ram_address: i64) -> Section {
    if ram_address >= 0x224978 {
      panic!("Target offset of dol is outside the bounds of the dol sections (0x8027C578+): {:X?}", ram_address);
    } else if ram_address >= 0x2200A0 {
      return Section::SDATA2;
    } else if ram_address >= 0x21F9E0 {
      return Section::SDATA;
    } else if ram_address >= 0x202C40 {
      return Section::DATA;
    } else if ram_address >= 0x1FA840 {
      return Section::RODATA;
    } else if ram_address >= 0x1FA820 {
      return Section::DTORS;
    } else if ram_address >= 0x1FA800 {
      return Section::CTORS;
    } else if ram_address >= 0x26C0 {
      return Section::TEXT;
    } else if ram_address >= 0x100 {
      return Section::INIT;
    } else {
      panic!("Target offset of dol is outside the bounds the of dol sections (0x100-): {:x?}", ram_address);
    }
  }
  