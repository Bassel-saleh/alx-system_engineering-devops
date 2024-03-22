# Using Puppet, created a manifest that kills a process named killmenow
exec { 'kill_killmenow_process':
  command => 'killp -f killmenow',
  path    => 'shell',
}
