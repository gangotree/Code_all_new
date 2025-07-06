# script for calculation of Rg
#!/bin/sh
Temp=310


echo 1 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-chain1-${Temp}T.xvg

echo 2 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-chain2-${Temp}T.xvg

echo 3 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-chain3-${Temp}T.xvg

echo 4 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-chain4-${Temp}T.xvg

echo 8 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-allchain-${Temp}T.xvg

echo 9 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-nolinkchain1-${Temp}T.xvg

echo 10 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-nolinkchain2-${Temp}T.xvg

echo 11 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-nolinkchain3-${Temp}T.xvg

echo 12 | gmx_mpi polystat -f nowater.xtc -s prod100-4c2lAu-${Temp}T.tpr -n index_${Temp}T.ndx -o Rg-nolinkchain4-${Temp}T.xvg



