# This manifest changes user limit to allow su command to work with the user
exec { 'change_hard':
  command => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
}

exec { 'change_soft':
  command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}
