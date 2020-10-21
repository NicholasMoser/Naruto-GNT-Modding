use std::env;

// The sections of the GNT4 dol.
enum Section {
    INIT,
    TEXT,
    CTORS,
    DTORS,
    RODATA,
    DATA,
    BSS,
    SDATA,
    SBSS,
    SDATA2,
    SBSS2,
}

// Takes in a ram address hex String, such as 800056F0 and returns the section and dol offset
// correlated with it. Do not include 0x before the hex String.
//
// # Example
//
// ```bash
// ram2dol 800056F0
// ```
//
fn main() {
    let arguments: Vec<String> = env::args().collect();
    if arguments.len() == 1 {
        println!("Please include ram address hex string argument.")
    } else if arguments.len() > 2 {
        println!("Please provide exactly one argument.")
    } else {
        let ram_address = i64::from_str_radix(&arguments[1], 16).unwrap();
        let section = get_section(ram_address);
        let subtract_amount = get_subtract_amount(section);
        let dol_offset = ram_address - subtract_amount;
        println!("Offset:  {:X}", dol_offset);
    }
}

// Get the amount to subtract from the ram address to get the offset. This depends on which
// section is referenced since some sections in the dol are skipped but are present in ram.
fn get_subtract_amount(section: Section) -> i64 {
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
    Section::BSS => panic!("Addresses in the bss section do not have an offset in the dol."),
    Section::SDATA => {
      println!("Section: SDATA");
      return 0x80056F40;
    },
    Section::SBSS => panic!("Addresses in the sbss section do not have an offset in the dol."),
    Section::SDATA2 => {
      println!("Section: SDATA2");
      return 0x80057C00;
    },
    Section::SBSS2 => panic!("Addresses in the sbss2 section do not have an offset in the dol.")
  };
}

// Get the section associated with this ram address.
fn get_section(ram_address: i64) -> Section {
    if ram_address >= 0x8027C578 {
      panic!("Target address of code is outside the bounds of the dol (0x8027C578+): {:X?}", ram_address);
    } else if ram_address >= 0x8027C560 {
      return Section::SBSS2;
    } else if ram_address >= 0x80277CA0 {
      return Section::SDATA2;
    } else if ram_address >= 0x80276FE0 {
      return Section::SBSS;
    } else if ram_address >= 0x80276920 {
      return Section::SDATA;
    } else if ram_address >= 0x802229E0 {
      return Section::BSS;
    } else if ram_address >= 0x80205C40 {
      return Section::DATA;
    } else if ram_address >= 0x801FD840 {
      return Section::RODATA;
    } else if ram_address >= 0x801FD820 {
      return Section::DTORS;
    } else if ram_address >= 0x801FD800 {
      return Section::CTORS;
    } else if ram_address >= 0x800056C0 {
      return Section::TEXT;
    } else if ram_address >= 0x80003100 {
      return Section::INIT;
    } else {
      panic!("Target address of code is outside the bounds the of dol (0x80003100-): {:x?}", ram_address);
    }
  }
  