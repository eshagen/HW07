# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

################################################################################

def cumulative_sum(list_):
	c_sum = []
	total = 0

	for num in list_:
		total += num
		c_sum.append(total)

	return c_sum



################################################################################
def main():


    pass

if __name__ == '__main__':
    main()