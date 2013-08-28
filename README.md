Facebook--Stalker--Analyzer
===========================

Analyzes the same bit of code that other Facebook Stalker apps would use but free of course

To use this you must have pyton 2.7.x installed in order to work because I used something that was added into that version of python and older versions wont work

How To Use
==========

First off I unfortunately cant figure out how to log into Facebook with python at the moment to do this so you guys will have to do some stuff in order to get started

First off log into your Facebook and view the source code of any page on Facebook and search for "InitialChatFriendsList"(with out the quotation marks)

While your looking at that area you'll be seeing something like this:
["InitialChatFriendsList",[],{"list":["112845672063384-3"]},26]

The part in the middle after {"list":[, with in the quotation marks(being 112845672063384) is a User-ID. What you have to do is take the user ID's and put them all in a text file called friends.txt and place each user ID on their own seperate line. If you dont do that it will not work at all and there will be alot of errors.
