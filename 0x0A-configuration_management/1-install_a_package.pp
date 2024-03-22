# install flask v(2.1.0)
# i don't know what's wrong
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
