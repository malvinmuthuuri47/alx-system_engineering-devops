# This manifest repplaces the ULIMIT to accommodate concurrent requests

file { '/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 2048"',
  replace => true,
}
