# helpers.py
# Contains methods for update_stdev, update_mean, update_brands

def update_stdev(m, std, n, x):
	diff = (newm - m)*(newm - m)*n+(x-newm)*(x-newm)
	return sqrt((std * std * n + diff)/(n+1))
	
def update_mean(m, std, n, x):
	return (m*n + x)/(n+1)
		
def update_brands
	# TO DO
	
def update_globals
	# TO DO
	
def update_successes
	# TO DO