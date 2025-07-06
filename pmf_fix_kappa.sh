#!/bin/bash
#PBS -l nodes=1:ppn=32
#PBS -l walltime=1000:00:00
#PBS -q long
#PBS -V
#PBS -o $PBS_O_WORKDIR/${PBS_JOBID%%.*}.out
#PBS -e $PBS_O_WORKDIR/${PBS_JOBID%%.*}.err


export UCX_TLS=tcp
module load gromacs/2021.4-p
module load intel/mpi/2021.8.0

source /opt/ohpc/pub/compiler/intel/compiler/2023.0.0/env/vars.sh intel164


# Set the number of threads per MPI rank
export OMP_NUM_THREADS=32

cd $PBS_O_WORKDIR

exe="/opt/ohpc/pub/apps/gromacs/2021.4-plumbed/bin/gmx_mpi"
mpi="/opt/ohpc/pub/compiler/intel/mpi/2021.8.0/bin/mpirun"
node="-machinefile ./a.txt -bootstrap=ssh -n 4"

##### Umbrella Sampling Calculation ###

foldername="COLVAR-K500"
kappa=8000.0
restmin=1.4
restmax=2.0
drest=0.1
ext=_5000
MDP="/data/gangotree/US/MDP"
rm -rf ${foldername}
mkdir ${foldername}

cp minim.gro ref.gro

for i in $(seq ${restmin} ${drest} ${restmax})
do

rm -rf $i$ext
mkdir $i$ext

echo -e ${foldername}'/COLVAR_'${i}' \t '${i}' \t '${kappa}' \t 0' >> ${foldername}/umbrelladatafile
cd ${i}${ext}

cat >plumed.dat << EOF
UNITS LENGTH=nm
rg: GYRATION TYPE=RADIUS ATOMS=1-762



restraint: RESTRAINT ARG=rg AT=${i} KAPPA=${kappa}

PRINT STRIDE=10 ARG=rg,restraint.bias FILE=COLVAR_${i}
EOF


gmx_mpi grompp -f $MDP/npt.mdp -c ../ref.gro -o eqb.tpr -p ../top-300T.top -v -maxwarn 2
gmx_mpi mdrun -deffnm eqb -plumed plumed.dat -nb cpu -ntomp ${OMP_NUM_THREADS}
gmx_mpi grompp -f $MDP/mdplincs.mdp -c eqb.gro  -o prod.tpr -p ../top-300T.top -v
gmx_mpi mdrun -deffnm prod -plumed plumed.dat -nb cpu -ntomp ${OMP_NUM_THREADS}
cd ..

cp ${i}${ext}/COLVAR_$i ${foldername}/COLVAR_$i
cp ${i}/prod.gro ref.gro

done
