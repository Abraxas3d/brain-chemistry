#/usr/bin/python2.7 $filename
from __future__ import print_function
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

print ("Hello! This makes molecule .pngs.")
print ("It creates a directory underneath wherever")
print ("we are called molecule_pngs and puts the drawings in there.")
print ("Then you move or copy them where you need them.")
print ("These are hardcoded files from Adam at the moment.")
print ("We need to come up with a naming convention for the molecules.")

m = Chem.MolFromMolFile('mdataq.sdf')
print (m)

suppl = Chem.SDMolSupplier('mdataq.sdf')
for mol in suppl:
	print("The number of atoms in molecule", mol, "is", mol.GetNumAtoms())
	
mols = [x for x in suppl]
print ("there are", len(mols),"molecules in this file.")

ms = [x for x in suppl if x is not None]

for m in ms:
	m2=Chem.AddHs(m)
	tmp = AllChem.Compute2DCoords(m2)

Draw.MolToFile(ms[0],'molecule_pngs/zero.png')
Draw.MolToFile(ms[1],'molecule_pngs/one.png')
Draw.MolToFile(ms[2],'molecule_pngs/two.png')
Draw.MolToFile(ms[3],'molecule_pngs/three.png')
Draw.MolToFile(ms[4],'molecule_pngs/four.png')
Draw.MolToFile(ms[5],'molecule_pngs/five.png')
Draw.MolToFile(ms[6],'molecule_pngs/six.png')
Draw.MolToFile(ms[7],'molecule_pngs/seven.png')
