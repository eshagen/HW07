# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


################################################################################

def is_sorted(list_):
	for item in list_:
		if (len(list_) <=1):
			return True
		if list_[0] > list_[1]:
			return False

		return is_sorted(list_[1:])

################################################################################
def main():

	a = [1, 2, 3, 7]
	print is_sorted(a)
    

if __name__ == '__main__':
    main()