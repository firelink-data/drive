docker images -a -q | % { docker image rm $_ -f }
