#!/usr/bin/env ruby
#Capture sender, reciever messages
puts ARGV[0].scan(/\[from:(\w+|+\d{11,11})\]\s\[to:(\w+|+\d{10,10})\]\s\[flags:-?\d:-?\d:-?\d:-?\d:-?\d\]/).join
