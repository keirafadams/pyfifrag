import argparse
from fragger import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='PyFiFragger',
        description='Fragmented File Writer',
        epilog='Created by Keira Adams, 2025')

    parser.add_argument("--frag_dir", required=True, type=str, help="Directory to store fragmented files")
    parser.add_argument("--frag_sz", default=8196, required=False, type=int, help="Size of fragment in byte to write")
    parser.add_argument("--frag_nr", default=32, required=False, type=int, help="Number of fragments to write by file")
    parser.add_argument("--nr_files", default=100, required=False, type=int, help="Number of files to write")

    args = parser.parse_args()

    frag_dir =  args.frag_dir
    frag_sz = args.frag_sz
    frag_nr = args.frag_nr
    nr_files = args.nr_files

    frag_data = data_gen(frag_sz)
    print("-----PyFiFragger-----")
    print("Target Directory: %s" % frag_dir)
    print("Number of Files: %d" % nr_files)
    print("Target Number of Fragments per File: %d" % frag_nr)
    print("Fragment Size: %d" % frag_sz)
    print("---------")
    core_frag(frag_dir, nr_files, frag_data, frag_nr)

