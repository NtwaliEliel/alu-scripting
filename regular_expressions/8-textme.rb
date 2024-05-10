#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([+]?\d{11,})\] \[to:([+]?\d{11,})\] \[flags:(-\d:\d:-\d:[-]?\d:-\d)\]/).join","
