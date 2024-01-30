#!/usr/bin/env ruby
#Capture sender, reciever messages
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
