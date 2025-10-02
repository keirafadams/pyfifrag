import os

def data_gen(frag_size):
    data_frag = os.urandom(frag_size)
    return data_frag

def core_frag(root_dir,nr_files,frag_data,nr_frags):
    print("Beginning file fragger run, depending on scale this may take a while...")
    for _ in range(nr_frags):
        for path_mod in range(nr_files):
                fullpath = "%s%s.frag" % (root_dir, path_mod)
                fhdl = open(fullpath, 'ab')
                fd = fhdl.fileno()
                fhdl.write(frag_data)
                os.sync()
                fhdl.close()
    print("Run Complete!")
if __name__ == "__main__":
    frag_sz = 8197
    nr_files = 1000
    nr_frags = 25

    frag_data = data_gen(frag_sz)
    frag_dir = "frag_test/"

    core_frag(frag_dir, nr_files, frag_data, nr_frags)



