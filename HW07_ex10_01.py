# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


################################################################################

def nested_sum(list_, total = 0):
	""" Accepts a list, sets a sum variable to zero, and returns the total sum 
	of all numbers in the list
	"""

	for entries in list_:
		if (type(entries) == list):
			total = nested_sum(entries, total)
		else:
			total += entries
	return total




################################################################################
def main():


    pass

if __name__ == '__main__':
    main()