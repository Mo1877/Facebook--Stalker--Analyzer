#!/usr/bin/python2.7

import collections
import urllib2

friends_file = open('friends.txt','r')

counter = collections.Counter()

for i in friends_file:
	counter[i] += 1

friends_file.close()

##Variables for number of messed up URL's
NumMessed_up_URL_HTTPError = 0
NumMessed_up_URL_URLError = 0
NumMessed_up_URL_GETURLERROR = 0

##Arrays for messed up URL's
Array_NumMessed_up_URL_HTTPError = []
Array_NumMessed_up_URL_URLError = []
Array_NumMessed_up_URL_GETURLERROR = []

##Array of working URL's
Array_Working_URL = []

for i in counter:
	i_new = str(i).rstrip('\n')
	print "User-ID: ", i_new

	##trying to access their facebook accounts
	try: 
		web = urllib2.Request('http://www.facebook.com/' + i_new)
		web2 = urllib2.urlopen(web)
		print web2.geturl() + '\n'
		Array_Working_URL.append(web2.geturl())

		##Checking for error's
		if web2.geturl() == "Not Found":
			NumMessed_up_GETURLERROR += 1
			Array_NumMessed_up_URL_GETURLERROR.append("http://www.facebook.com/" + i_new)
		else:
			pass

	except urllib2.HTTPError as e:
		##Checking for error's
		if e.reason == 'Not Found':
			NumMessed_up_URL_HTTPError += 1
			Array_NumMessed_up_URL_HTTPError.append("http://www.facebook.com/" + i_new)
		else:
			pass
		
		print e.reason + '\n'

	except urllib2.URLError as e:
		##Checking for error's
		if e.reason == 'Not Found':
			NumMessed_up_URL_URLError += 1
			Array_NumMessed_up_URLError.append("http://www.facebook.com/" + i_new)
			
		else:
			pass

		print e.reason + '\n'





##Error's
TotalErrors = NumMessed_up_URL_GETURLERROR + NumMessed_up_URL_HTTPError + NumMessed_up_URL_URLError
print "Number of Errors: ", TotalErrors


print "Number of messed up URL's by geturl(): ", NumMessed_up_URL_GETURLERROR
print "Number of messed up URL's by HTTPError's: ", NumMessed_up_URL_HTTPError
print "Number of messed up URL's by URLError's: ", NumMessed_up_URL_URLError 
print "NOTE: These errors are bassed by the feedback from the program saying 'Not Found' when trying to access the url by the accounts ID\n" 

print "These links may not work due to networking or something of that kind preventing the program to see the see the accounts or they're possibly blocked for the public to see.\n"

##Putting out messed up urls
print "Array of messed up URL's by geturl(): ", Array_NumMessed_up_URL_GETURLERROR, "\n"
print "Array of messed up URL's by HTTPError: ", Array_NumMessed_up_URL_HTTPError, "\n"
print "Array of messed up URL's by URLError: ", Array_NumMessed_up_URL_URLError, "\n"
print "Try to manually access any URL's that were proven broken by the program while logged in on Facebook.\n"



##Array's of URL's that work
print "Array's of working URL's: ", Array_Working_URL, '\n'

##Exporting result's
print "About to exporting result's...\n"

results = open('results.txt', 'w')

print "Exporting results..."

##Exporting number of errors
results.write('Total Errors: ' + str(TotalErrors) + '\n\n')
results.write("Number of messed up URLs by geturl(): " + str(NumMessed_up_URL_GETURLERROR) + "\n")
results.write("Number of messed up URLs by HTTPError: " + str(NumMessed_up_URL_HTTPError) + '\n')
results.write("Number of messed up URLs by URLError: " + str(NumMessed_up_URL_URLError) + '\n')

results.close()
##Exporting array of errors to their seperate folders and files


##Exporting array of errors by geturl
results_Array_GETURLERROR = open('Errors_geturl.txt', 'w')
for i in Array_NumMessed_up_URL_GETURLERROR:
	results_Array_GETURLERROR.write(i)

results_Array_GETURLERROR.close()


##Exporting array of errors by HTTPError
results_Array_HTTPError = open('Errors_HTTPError.txt', 'w')
for i in Array_NumMessed_up_URL_HTTPError:
	results_Array_HTTPError.write('\n'+i)

results_Array_HTTPError.close()

##Exporting array of errors by URLError
results_Array_URLError = open('Errors_URLError.txt', 'w')
for i in Array_NumMessed_up_URL_URLError:
	results_Array_URLError.write('\n' + i)

results_Array_URLError.close()


##Exporting working URLs
results_Array_WorkingURLS = open('WorkingURLS.txt', 'w')
for i in Array_Working_URL:
	results_Array_WorkingURLS.write('\n' + i)

results_Array_WorkingURLS.close()

print "Exporting results finished..."