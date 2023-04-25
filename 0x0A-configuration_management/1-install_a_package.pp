# Installing flask Version 2.1.0 using puppet from pip3

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip',
}
