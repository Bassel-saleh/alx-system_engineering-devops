# Using Puppet, created a manifest that kills a process named killmenow
exec { 'pkill':
  command => 'killp killmenow',
  path    => 'shell',
}
