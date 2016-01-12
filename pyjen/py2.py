from sys import argv

script, user_name = argv
prompt = '>'


print " Hi i'm %s, It is my script %s" % (user_name, script)
print "It's my very first script"
print "I would like to ask some Q's %s" % user_name

name = raw_input(prompt)


print "Where do you live %s?" % user_name

location = raw_input(prompt)



print """ 
	have u done with ur Q's?
	.......let me know if u have any concerns %s
	.......come again wt's urname: %r.....
	.......wr u live %r: 
	
	"""  % (user_name, name, location)