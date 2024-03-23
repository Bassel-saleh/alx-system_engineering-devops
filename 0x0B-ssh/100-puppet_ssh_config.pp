# Setting up ssh configg file with no password and private key location
include stdlib
file_line { 'passphrase auth off':
  ensure  => present,
  line    => '     PasswordAuthentication no',
  path    => 'etc/ssh/ssh_config',
  replace => true,
}

file_line { 'identity file':
  ensure  => present,
  line    => '     IdentityFile ~/.ssh/school',
  path    => 'etc/ssh/ssh_config',
  replace => true,
}
