 git branch --merged | egrep -v "(^\*|master|dev|staging|release)"  | xargs git branch -d
