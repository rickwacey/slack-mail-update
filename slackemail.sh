#!/bin/bash

TOKEN="add_token_here"
USER_EMAILS="$(curl -X GET -H "Content-Type: application/x-www-form-urlencoded" https://slack.com/api/users.list?token=${TOKEN} | jq -r .members[].profile.email)"
USER_ID="$(curl -X GET -H "Content-Type: application/x-www-form-urlencoded" https://slack.com/api/users.list?token=${TOKEN} | jq -r .members[].id)"

USER_EMAILS=(${USER_EMAILS// / })
USER_ID=(${USER_ID// / })
length=${#USER_EMAILS[@]}

for ((i=0;i<=$length;i++)); do
        echo -e "${USER_EMAILS[$i]},${USER_ID[$i]}"
done