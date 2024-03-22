# install flask v(2.1.0)

package { 'python3.8.1-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
