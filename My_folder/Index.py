import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table

# 1. Load the data
data = Table.read('4fgl_j0808.2-0751_lightcurve.fits')

# 2. Extract specific parameters based on your Index list
# Index 0 is 'norm' (Flux), Index 1 is 'alpha' (Spectral Index)
flux_vals = data['param_values'][:, 0]
flux_errs = data['param_errors'][:, 0]

alpha_vals = data['param_values'][:, 1]
alpha_errs = data['param_errors'][:, 1]

# 3. Use MJD Midpoints
mjd_center = (data['tmin_mjd'] + data['tmax_mjd']) / 2.0

# 4. Create the Dual Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Top Plot: Normalization (Flux)
ax1.errorbar(mjd_center, flux_vals, yerr=flux_errs, fmt='ko', capsize=2, label='Norm')
ax1.set_ylabel('Normalization (norm)')
ax1.set_title('PKS 0805-07: LogParabola Evolution')
ax1.grid(True, alpha=0.3)

# Bottom Plot: Alpha (Spectral Index)
ax2.errorbar(mjd_center, alpha_vals, yerr=alpha_errs, fmt='ro', capsize=2, label='Alpha')
ax2.set_ylabel(r'Spectral Slope ($\alpha$)')
ax2.set_xlabel('Time (MJD)')
ax2.grid(True, alpha=0.3)

# Handle potential NaNs for better limits
ax2.set_ylim(np.nanmin(alpha_vals)-0.2, np.nanmax(alpha_vals)+0.2)
plt.savefig('Index.png', dpi=300)
plt.tight_layout()
plt.show()
