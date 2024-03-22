# Using Puppet, created a manifest that kills a process named killmenow
exec { 'pkill':
  command => 'killp -f killmenow',
  path    => 'shell',
}
