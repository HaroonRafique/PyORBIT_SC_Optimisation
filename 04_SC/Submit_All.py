import os

master_dir = os.getcwd()

Sims_01 = True
Sims_02 = True

sbs_locations = []
sbs_locations.append('/01_Original_01/')
sbs_locations.append('/01_Original_02/')
sbs_locations.append('/01_Original_03/')
sbs_locations.append('/01_Original_04/')
sbs_locations.append('/01_Original_05/')
sbs_locations.append('/01_Original_06/')
sbs_locations.append('/01_Original_07/')
sbs_locations.append('/01_Original_08/')

if Sims_01:
	for loc in sbs_locations:
		print '-------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: Original PyORBIT, Nodes = ', loc[14]
		print '-------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

sims02_locations = []
sims02_locations.append('/02_LessMPI_01/')
sims02_locations.append('/02_LessMPI_02/')
sims02_locations.append('/02_LessMPI_03/')
sims02_locations.append('/02_LessMPI_04/')
sims02_locations.append('/02_LessMPI_05/')
sims02_locations.append('/02_LessMPI_06/')
sims02_locations.append('/02_LessMPI_07/')
sims02_locations.append('/02_LessMPI_08/')

if Sims_02:
	for loc in sims02_locations:
		print '-------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: Less MPI PyORBIT, Nodes = ', loc[14]
		print '-------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)
