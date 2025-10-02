# pyfifrag
A utility to create deliberately fragmented files for filesystem and 
storage media testing.

## Why this widget!?
Many file systems and low level storage devices (eg HDDs and SSDs) are
optimized for reading and writing data in large _extents_. That is a
single contiguous block. This utility is designed to pathologically
bypass that to aid in stress testing devices and filesystems with 
pathological layouts.

Right now we only support fire-hosing a single
directory from the core driver, but this can easily be extended
to create arbitrary file trees.

## Usage

``
python3 pyfifragger.py [-h] --frag_dir FRAG_DIR [--frag_sz FRAG_SZ] [--frag_nr FRAG_NR] [--nr_files NR_FILES]
``

### option details

* frag_dir: required, path to directory to write fragmented files
* frag_sz: size in bytes of the fragments to write, default 8196
* frag_nr: number of fragments to write per file, default 32
* nr_files: number of files in total to write, default 100

## Verifying file fragmentation

On linux systems, this can be done using the FIEMAP manually, or using a utility such as ``filefrag``

For example, one of the files from a run with the provided defaults might produce a 256KiB file
with extensive fragmentation

``
File size of 99.frag is 262272 (65 blocks of 4096 bytes)
 ext:     logical_offset:        physical_offset: length:   expected: flags:
   0:        0..       2:  136680862.. 136680864:      3:
   1:        3..       4:  133832674.. 133832675:      2:  136680865:
   2:        5..       6:  136751120.. 136751121:      2:  133832676:
   3:        7..       8:  136982205.. 136982206:      2:  136751122:
   4:        9..      10:  136751278.. 136751279:      2:  136982207:
   5:       11..      12:  136982327.. 136982328:      2:  136751280:
   6:       13..      14:  136750452.. 136750453:      2:  136982329:
   7:       15..      16:  133828502.. 133828503:      2:  136750454:
   8:       17..      18:  133831153.. 133831154:      2:  133828504:
   9:       19..      20:  133826416.. 133826417:      2:  133831155:
  10:       21..      22:  133828412.. 133828413:      2:  133826418:
  11:       23..      24:  133830514.. 133830515:      2:  133828414:
  12:       25..      26:  133828260.. 133828261:      2:  133830516:
  13:       27..      28:  133830226.. 133830227:      2:  133828262:
  14:       29..      30:  133830394.. 133830395:      2:  133830228:
  15:       31..      32:  133831263.. 133831264:      2:  133830396:
  16:       33..      34:  133829726.. 133829727:      2:  133831265:
  17:       35..      36:  133831331.. 133831332:      2:  133829728:
  18:       37..      38:  133827812.. 133827813:      2:  133831333:
  19:       39..      40:  133831742.. 133831743:      2:  133827814:
  20:       41..      42:  133832212.. 133832213:      2:  133831744:
  21:       43..      44:  133832402.. 133832403:      2:  133832214:
  22:       45..      46:  133831569.. 133831570:      2:  133832404:
  23:       47..      48:  133827918.. 133827919:      2:  133831571:
  24:       49..      50:  133829900.. 133829901:      2:  133827920:
  25:       51..      52:  133830090.. 133830091:      2:  133829902:
  26:       53..      54:  133832850.. 133832851:      2:  133830092:
  27:       55..      56:  133833038.. 133833039:      2:  133832852:
  28:       57..      58:  133833226.. 133833227:      2:  133833040:
  29:       59..      60:  133833414.. 133833415:      2:  133833228:
  30:       61..      62:  133833600.. 133833601:      2:  133833416:
  31:       63..      64:  133833800.. 133833801:      2:  133833602: last,eof
  ``



