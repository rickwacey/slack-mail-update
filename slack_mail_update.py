#This is a tool to update Slack email addresses from one domain to another. It needs an email_upload.txt file output from slackemail.sh to run


from slackclient import SlackClient
import json

#get token from https://api.slack.com/custom-integrations/legacy-tokens and add to slack_token
slack_token = "add_token_here"
sc = SlackClient(slack_token)


#if an entry with the domain is found in the text file, it replaces the domain, makes the api call to set it and then prints that the mail was changed. If the domain doesn't match then it skips.
with open("email_upload.txt") as inFile:
	for line in inFile:
		userInfo = line.split(',')

		if "olddomain.com" in userInfo[0]:

			userNewEmail = userInfo[0].replace("olddomain.com","newdomain.com")

			emailjson = {
		
				"email": userNewEmail
			}

			sc.api_call(
			"users.profile.set",
			user=userInfo[1].rstrip(),
			profile=emailjson
				)
		
			print "User ID " + userInfo[1].rstrip() + " changed email to " + userNewEmail

		else:

			print "Skipping: " + userInfo[0]
