def get_final_line(filename):
	final_line = ''
	for current_line in open(filename):
		final_line = current_line
	return final_line

print(get_final_line('D:\\RnD\\python-dev\\Python_Workout\\Ch05_Files\\sample_log.txt'))