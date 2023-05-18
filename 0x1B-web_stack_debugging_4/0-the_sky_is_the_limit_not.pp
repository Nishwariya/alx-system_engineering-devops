# Increase the number of open files limit

$command='sed -i \'/^ULIMIT/c\ULIMIT="-n 4096"\' /etc/default/nginx'
exec {'increase nofile limit':
    command => $command,
    path    => ['/bin', '/usr/bin']
}

# ensure nginx is running and restart after change
service {'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => Exec['increase nofile limit']
}
