import os
import sys

filepath = os.path.dirname(os.path.abspath("__file__"))
print('Adding ' + filepath + ' to path')
sys.path.append(filepath)

import cubit
from utils import find_claro

print("Groups to Blocks and Materials")

print(find_claro())

for (name, gid) in cubit.group_names_ids():
    # skip the 'picked' group and other groups
    # that aren't materials
    if name == 'picked' or 'mat' not in name:
        continue
    mat = name.split('/')[0].split(':')[1]

    if not mat:
        print(f'WERID MAT: {mat}')
        continue
    # get all volumes and bodies for this group
    volumes = cubit.get_group_volumes(gid)
    bodies = cubit.get_group_bodies(gid)

    # create a new block
    block_id = cubit.get_next_block_id()
    cmd = f'create block {block_id}'
    cubit.cmd(cmd)
    if len(volumes) != 0:
        vols = " ".join([str(v) for v in volumes])
        cmd = f'block {block_id} add volume {" ".join(volumes)}'
        cubit.cmd(cmd)
    if len(bodies) != 0:
        bods = " ".join([str(b) for b in bodies])
        cmd = f'block {block_id} add body {bods}'
        cubit.cmd(cmd)
    # create a new material with the material identifier for
    # this group
    cmd = f'create material name "{mat}"'
    cubit.cmd(cmd)
    # assign the new material to the mesh group
    cmd = f'block {block_id} material "{mat}"'
    cubit.cmd(cmd)
