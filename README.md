# unified_structure_format

A unified file format for all kinds of molecule structure. Including protein, small molecule, crystal.

## Requirement

Only `numpy`

Recommended `matplotlib` for visualization

## File format

Unified file format including these subtypes, with no actual difference:
- General format `.usf`
- For protein (only heavy atom) `.usfpro`
- For protein (all atom) `usfproh`
- For crystal `usfxta`
- For molecule `usfmol`


A `.usf` file is a python pickle file. 

Necessary features:

- `name`
- `atom_type`: (N_atom * 1)
- `coordinate`: (N_atom * 3)

Optional features:

- `atom_index`: (N_atom * 1), must identical to `np.arange(0,N_atom)`
- `bond`: (N_bond, 2), e.g. (index_1, index_2)
- `atom_name`: (N_atom * 1), only for protein, e.g. "CA"
- `res_index`: (N_atom * 1), only for protein




