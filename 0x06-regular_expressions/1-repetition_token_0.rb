#!/usr/bin/env ruby
#Match "hbt+n" str
puts ARGV[0].scan(/hbt{2,5}n/).join
