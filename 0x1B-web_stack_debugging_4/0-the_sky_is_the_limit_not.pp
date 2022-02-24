-- This confu=igures nginx server to handle more
-- requests
exec { 'fix failing requests':
  command => 'sed -i s/worker_processes 4;/ worker_processes 9;/g' /var/www/html/wp-settings.php; service nginx restart,
  path    => ['usr/bin/', '/bin', '/usr/sbin']
}
