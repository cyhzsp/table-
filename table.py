import math
def form (tab_w=5,tab_h=5,tab_fork=None,*,border_style="round"):
	#tab_fork
	if tab_fork == None or tab_fork == []:
		tab_fork=[-114,-514]
	the_table=""
	#border-style
	if border_style == "round":
		tab_head="╭"
		tab_last_head="╰"
		tab_end="╮"
		tab_last_end="╯"
	elif border_style == "fangzheng":
		tab_head="┌"
		tab_last_head="└"
		tab_end="┐"
		tab_last_end="┘"
	#table-line 1
	the_table+=tab_head
	for i in range(1,tab_w-2):
		times=0
		for j in tab_fork:
			if i == j-1:
				the_table+="┬"
				times=1
		if i != j-1 and times == 0:
			the_table+="─"
			times=1
	the_table+="─"
	the_table+=tab_end
	the_table+="\n"
	#table-line 2
	value=int(math.floor(tab_w/2))
	equal=""
	for i in range(0,tab_w):
		if the_table[i] == "╭" or the_table[i] == "┌":
			the_table+="│"
			equal+="│"
		elif the_table[i] == "╮" or the_table[i] == "┐":
			the_table+="│"
			equal+="│"
		elif the_table[i] == "─":
			the_table+="  "
			equal+="  "
		elif the_table[i] == "┬":
			the_table+="│"
			equal+="│"
		else:
			the_table+="?"
			equal+="?"
	#table line 2+N (2+N<last)
	for i in range(2,tab_h-1):
		the_table+="\n"
		the_table+=equal
	#table line last (last line)
	the_table+="\n"
	the_table+=tab_last_head
	for i in range(1,tab_w-2):
		times=0
		for j in tab_fork:
			if i == j-1:
				the_table+="┴"
				times=1
		if i != j-1 and times == 0:
			the_table+="─"
			times=1
	the_table+="─"
	the_table+=tab_last_end
	the_table+="\n"
	return the_table
def main ():
	print("You can make a form!")
if __name__ == "__main__":
	main()
