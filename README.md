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


