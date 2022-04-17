import copy
clusters = {
	0: [[0]],
	1: [[1]]
}

def add_num_to_dict(num):
	global clusters
	running_list = []
	for i in range(1, num+1):
		for combos in clusters[num-i]:
			for p in combos:
				running_list.append([i,p])
	clusters[num] = [running_list]

num_of_users = int(input("Enter the number of users: "))
print("\n")

for num in range(2, num_of_users+1):
	add_num_to_dict(num)

for key in clusters.keys():
	print("---- Clusters for ", key, " Users are---------")
	for i in clusters[key]: 
		print(i)
		print("Total Clusters: ", len(i), "\n")