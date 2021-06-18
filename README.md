# to (Alfa)

## a todo list manager in command line.

> ## **_Description_**:
> 
>	this program is useful to list your todo.
>	everywhere this program run, it will make a file named '.to' in the
>	directory that runed in.
>	this file is the database of the program in a kind of json format, more
>	like a dictionary in python.
>	
>	there are too many project that you contribute in them.
>	and there are too many feacher that you should impiment.
>	or there are a lots of bug that should fixed.
>	whene you use a triditional todo-list manager. you have a file which 
>	you write your todo in there and you have to indicate which task is for 
>	what project.
>	but with this program you dont need to do that. easy add your list
>	in the directory of that project.
>	and any time that you need to know what you should do for what project
>	go to the progect directory and write the coresponding command.
>	ok the concept of the .to file was just this. but what about the list?
>	
>	a to-list is use to list and seprate the task from each other.
>	for example you have 5 bugs to fix and there are 6 feacher that should
>	impliment to your project. with a list of 'to' you can easily add your
>	task in the coresponding list. in this case we have bugs and feacher
>	so we can have two list: fix and add
>	in fix list we will add the bug which should fix.
>	in add list we will add feacher that should add.
>	
>	the other reasen that list's are useful is to mention someone.
>	for example if i want to assign some task to one person of the team all i need to do
>	is that make a list that start with '@' and name of that person. like: @m_shaben
>	this feacher in the fuchure can be use to send the list to that person just after
>	it definded. or may can send to the email just by assign the task to an email.
>

---

> ### __how to install__
> - ``` cd /opt ```
> - ``` git clone https://github.com/DistroTEAM/to.git ```
> - ``` chmod -R 777 /opt/to ```
> - ``` ln /opt/to/to ~/.locale/bin/to ```
> - ``` to ```
---

 ### Usage
 >
 > - adding:
                ```add```         		add a new to
                ```insert```      	insert a task under a to
                ```edit```   		    edit a task or to
   >---
   > - done:
                ```fill```        	completion an entire to
                ```done```        	done one task from a to
                ```undone```      	undone one task
   >---
> - print:
                ```list```        print all todo's
                ```show```        show task's wich you doneprogress:
   > ---
   > - progress
			   ```prog```        	show a percentage and a progress of what you done
			   ```log```         	show a log of what you done.
