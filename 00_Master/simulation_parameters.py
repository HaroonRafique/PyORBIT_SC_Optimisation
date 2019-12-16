import numpy as np

parameters = {}

parameters['Beam']						= 'BCMS' #'Nominal'
parameters['Machine']					= 'PreLIU' #'LIU'

parameters['tunex']						= '621'
parameters['tuney']						= '610'

parameters['lattice_start'] 		= 'BWSV64'
parameters['n_macroparticles']			= int(5E2)

# PS Injection 1.4 GeV
if parameters['Machine'] is 'PreLIU':
	parameters['gamma'] 	= 2.49038064
	if parameters['Beam'] is 'Nominal':
		parameters['intensity']			= 16.84E+11
		parameters['epsn_x']			= 2.25E-6
		parameters['epsn_y']			= 2.25E-6
		parameters['bunch_length']		= 180e-9
		parameters['blength']			= 180e-9
		parameters['dpp_rms']			= 0.9E-03
		parameters['rf_voltage']		= 0.0251 # 25.1 kV
	elif parameters['Beam'] is 'BCMS':
		parameters['intensity']			= 8.05E+11
		parameters['epsn_x']			= 1.2E-6
		parameters['epsn_y']			= 1.2E-6
		parameters['bunch_length']		= 150e-9
		parameters['blength']			= 150e-9
		parameters['dpp_rms']			= 0.8E-03
		parameters['rf_voltage']		= 0.0212 # 21.2 kV
# PS Injection 2 GeV
elif parameters['Machine'] is 'LIU':
	parameters['gamma'] 	= 3.131540798
	if parameters['Beam'] is 'Nominal':
		parameters['intensity']			= 32.5E+11
		parameters['epsn_x']			= 1.8E-6
		parameters['epsn_y']			= 1.8E-6
		parameters['bunch_length']		= 205e-9
		parameters['blength']			= 205e-9
		parameters['dpp_rms']			= 1.5E-03
		parameters['rf_voltage']		= 0.0418 # 41.8 kV
	elif parameters['Beam'] is 'BCMS':
		parameters['intensity']			= 16.25E+11
		parameters['epsn_x']			= 1.43E-6
		parameters['epsn_y']			= 1.43E-6
		parameters['bunch_length']		= 135e-9
		parameters['blength']			= 135e-9
		parameters['dpp_rms']			= 1.1E-03
		parameters['rf_voltage']		= 0.03655 # 36.55 kV

parameters['beta'] 		= np.sqrt(parameters['gamma']**2-1)/parameters['gamma']
parameters['LongitudinalJohoParameter'] = 1.2
parameters['LongitudinalCut'] 	= 2.4
parameters['TransverseCut']		= 5
parameters['circumference']		= 2*np.pi*100
parameters['phi_s']				= 0
parameters['macrosize']			= parameters['intensity']/float(parameters['n_macroparticles'])
parameters['tomo_file']			='Tomo_Files/PyORBIT_Tomo_file_'+parameters['Beam']+'_'+parameters['Machine']+'.mat'

c 						= 299792458
parameters['sig_z'] 	= (parameters['beta'] * c * parameters['blength'])/4.

parameters['turns_max'] = int(50)


switches = {
	'CreateDistn':		True,
	'Update_Twiss':		False,
	'Space_Charge': 	True,
	'Outputs':			False,
	'GridSizeX': 128,
	'GridSizeY': 128,
	'GridSizeZ': 64
}


if switches['Outputs'] is True:
	tu = parameters['turns_max']
else:
	tu = range(0, parameters['turns_max'])

parameters['turns_print'] = sorted(tu)
parameters['turns_update'] = sorted(tu)

# PTC RF Table Parameters
harmonic_factors = [1] # this times the base harmonic defines the RF harmonics (for SPS = 4620, PS 10MHz 7, 8, or 9)
time = np.array([0,1,2])
ones = np.ones_like(time)
Ekin_GeV = 1.4*ones
RF_voltage_MV = np.array([parameters['rf_voltage']*ones]).T # in MV
RF_phase = np.array([np.pi*ones]).T

RFparameters = {
	'harmonic_factors': harmonic_factors,
	'time': time,
	'Ekin_GeV': Ekin_GeV,
	'voltage_MV': RF_voltage_MV,
	'phase': RF_phase
}
