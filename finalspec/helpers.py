# helpers.py
# Contains methods for updating everything

def update(m, std, n, x):
	newm = (m*n + x)/(n+1)
	diff = (newm - m)*(newm - m)*n+(x-newm)*(x-newm)
	newstd = sqrt((std * std * n + diff)/(n+1))
	return (newm, newstd)
		
def update_brands
	# TO DO
	
def update_globals
	# TO DO
	
def update_successes
	# TO DO