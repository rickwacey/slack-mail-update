# slack-mail-update
A small script to update Slack email addresses in bulk from one domain to another.

Dependency needed: Slack Developer kit for Python (https://github.com/slackapi/python-slackclient). Install this first.

Usage:

1. Get a token from https://api.slack.com/custom-integrations/legacy-tokens for the slack environment where you want to change some of the email domains in bulk. You need to be an admin in your slack instance to do this.
2. Replace "add_token_here" string in both slack_mail_update.py and slackemail.sh with the token you created (e.g. "14x439347xsadsa")
3. Run slackemail.sh to get all your email and user IDs from the your slack environment and output to a text file email_upload.txt
	bash slackemail.sh > email_upload.txt
4. Replace the olddomain.com (in 2 places) and newdomain.com (in 1 place) strings in slack_mail_update.py with the domain you want to change from and to.
5. Run the python script (./slack_mail_update.py)
6. Note every user will get an email stating that their address has been changed.