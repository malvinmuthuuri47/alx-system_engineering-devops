#This puppet script increases the ulimit
exec {'increase ulimit':
  command => 'sed -i "s/15/2500/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart nginx
exec {'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
