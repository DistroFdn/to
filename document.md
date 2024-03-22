Concept:
- this program is usefull to list your todo.
	enywhere this program run, it will make a file named '.to' in the
	directory that runed in.
	this file is the database of the program in a kind of json format, more
	like a dictionary in python.
	
	there are too many project that you contribute in them.
	and there are too many feacher that you should impiment.
	or there are a lots of bug that should fixed.
	whene you use a triditional todo-list manager. you have a file which 
	you write your todo in there and you have to indicate which task is for 
	what project.
	but with this program you dont need to do that. easy add your list
	in the directory of that project.
	and any time that you need to know what you should do for what project
	go to the progect directory and write the coresponding command.
	ok the concept of the .to file was just this. but what about the list?
	
	a to-list is use to list and seprate the task from each other.
	for example you have 5 bugs to fix and there are 6 feacher that should
	impliment to your project. with a list of 'to' you can easily add your
	task in the coresponding list. in this case we have bugs and feacher
	so we can have two list: fix and add
	in fix list we will add the bug which should fix.
	in add list we will add feacher that should add.
	
	the other reasen that list's are useful is to mention someone.
	for example if i want to assign some task to one person of the team all i need to do
	is that make a list that start with '@' and name of that person. like: @m_shaben
	this feacher in the fuchure can be use to send the list to that person just after
	it definded. or may can send to the email just by assign the task to an email.


Module's:
	to.py:
		this is the main of the program.
		the main control all other module's.
		the intractive and non-intractive command-line implimented in this file.

	core.py:
		all the function that work with '.to' file is implimented in this file.
		there is a class that use to print colorized output according to task priority.

	initer.py:
		any user that use this program should say who is it.
		this informatin is use to log who done what.
		there are just a email and a username that should store in a file.
		the file in the linux-base will be in ~/.local/share/to.conf
		and in windows system it will be in the [user-home-dir]/to.conf
		and what this function is do 
		first is check the file is exist or not.
		second this function will get username and email and then create the file.

Function's:
	Uconf:
		every time that we need to save who done what. whe call this function
		to read the email and usernam form 'to.conf' and return a tuple of them.

	AddTo:
		add a list of to.
		like: fix, add, make, run, get, watch, listen, etc.	  
	CheckFile:
		this functin will check the .to is exist or no.
		if exist. it will let program continu.
		if not, and the parametr init==True, this function will create the file.
		if init==false program will exit with status 2
		init indicate that the program is initializing or no.
		
	Clear:
		in intractive mode we need to clear the screen. this function will do that.
  
	Commit:
		to commit the last task text as git commit message.
		this function will run this command 'git commit -m YYY'
		instead of YYY will be the latest task text

	CompletTo:
		to complete an entire list of task.
		after mark all as done, all the task text in the list will return as a list.

	Done:
		any time that user done one task.
		the task text should save in a tag called 'latest'
		this function will save the task text in that tag if the function it got return text
		the text of the task will come from DoneTask() and CopleteTo()

	DoneTask
		done a task. but never call directly.
		this functin will return a string of the the task text

	Edit:
		edit a task.

	GetDate:
		any time that we need to get a deadline of a task from user.
		this function will get them and return a dictionary of
		year, month, day
		 
	InsertTask:
		function to add a task in a list of task.

	MenuIntractive:
		this is the help for the intractive menu

	MenuNonIntractive:
		command of intractive and non-intractive cli is differnt so we have to print the
		help that corespond.

	PrintDone:
		show the task's which doned.

	PrintTask:
		list the task that user should to do.
  
	Progress:
		will read the '.to' file and gave the information of percent of doned task's
		to Bar().
	SetDate:
		to get the towday date in dictionary format.

	TColor:
		this is a class that have some string varibale that store teminal-color code.
		the variable will use whene we need to print a colorized output.

	TimeLeft:
		whenever that we need to show to user how much day do we have to reach the 
		deadline, this function will use.
  
	UnDoneTask:
		this function will undone a doned task
 	
	Bar:
		bar get a max and min, then will print a progressbar of percent of doned task.
