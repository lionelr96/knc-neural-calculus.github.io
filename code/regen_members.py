from knc_web_tools import *

def main():
	user_info = load_user_info()

	mempage = gen_members_page(user_info)

	do_continue = input('WARNING: this will overwrite the old `../members.html`, continue? (y/n)\n')

	if do_continue == 'n':
		exit()
	elif do_continue == 'y':
		with open("../members.html", 'w') as f:
			print(mempage, file=f)

if __name__ == "__main__":
	main()