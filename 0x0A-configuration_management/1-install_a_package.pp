# Installs flask v2.1.0 with pip3
package { 'Flask':
  ensure   => ['2.1.0' , created],
  provider => 'pip3',
}
