def worstFit(blockSize, m, processSize, n): 
	
	# Stores block id of the block 
	# allocated to a process 
	
	# Initially no block is assigned 
	# to any process 
	allocation = [-1] * n 
	
	# pick each process and find suitable blocks 
	# according to its size ad assign to it 
	for i in range(n): 
		
		# Find the best fit block for 
		# current process 
		wstIdx = -1
		for j in range(m): 
			if blockSize[j] >= processSize[i]: 
				if wstIdx == -1: 
					wstIdx = j 
				elif blockSize[wstIdx] < blockSize[j]: 
					wstIdx = j 

		# If we could find a block for 
		# current process 
		if wstIdx != -1: 
			
			# allocate block j to p[i] process 
			allocation[i] = wstIdx 

			# Reduce available memory in this block. 
			blockSize[wstIdx] -= processSize[i] 

	print("Process No. Process Size Block no.") 
	for i in range(n): 
		print(i + 1, "		 ", 
			processSize[i], end = "	 ") 
		if allocation[i] != -1: 
			print(allocation[i] + 1) 
		else: 
			print("Not Allocated") 

if __name__ == '__main__': 
	blockSize = list(map(int, input("Enter memory block sizes (comma-separated): ").split(',')))
	m = len(blockSize) 
	processSize = list(map(int, input("Enter process sizes (comma-separated): ").split(',')))
	n = len(processSize) 

	worstFit(blockSize, m, processSize, n) 

