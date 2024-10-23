#!python
import numpy as np
import sys

import cubit

def compute_tri_surf_dist_err(surface_id=None):
    """Compute the maximum distance between a surface's triangles the closest point on a surface."""

    if surface_id is None:
        S = cubit.get_entities( "surface" )
    else:
        S = [surface_id]

    if len(cubit.get_entities("tri")) == 0:
        raise ValueError("No triangles found in the model.")

    out = -1.0
    for sid in S:
        surface = cubit.surface( sid )
        T = cubit.parse_cubit_list( "tri", f"in surface {sid}" )
        tri_surf_dists = np.zeros(len(T), dtype=np.float64)
        for i, tid in enumerate(T):
            tri_center = np.array(cubit.get_center_point("tri", tid), dtype=np.float64)
            surf_loc = np.array(surface.closest_point_trimmed(tri_center), dtype=np.float64)
            tri_surf_dist = np.sqrt(np.sum((tri_center - surf_loc)**2))
            tri_surf_dists[i] = tri_surf_dist
            max_tri_surf_dist = np.max(tri_surf_dists)
        out = max(out, max_tri_surf_dist)
    return out





max_tri_surf_dist = compute_tri_surf_dist_err()
print("###############################################")
print("Max tri-surf dist: {}".format(max_tri_surf_dist))
print("###############################################")


