
# echo from .bashrc screws up scp .. alas
#if [ -n "$INSIDE_EMACS" ]; then 
#  echo Hello Emacs
#fi
umask 0007
export HOME=$(/usr/local/bin/home)

export PS1='\n$(/usr/local/bin/Z)\n\u@\h§\w§\n> '
export PS2='>>'

export PATH=~/bin:~/.local/bin:"$PATH"
export PS_FORMAT=user:15,pid,%cpu,%mem,vsz,rss,tty,stat,start,time,command
export EDITOR=emacs

alias pcd_ac="~/bin/discourse_application_client/start"
alias pcd_as="~/bin/discourse_application_server/start"

alias pcd_hcj="/home/reasoning-technology_html-css-js/bin/start"
alias pcd_cg="/home/customer_gateway_dev/bin/start"
