# this manifest kills process Killmenow

exec {'kill proess killmenow':
    command => 'pkill killmenow',
    path => '/usr/bin/'
}
