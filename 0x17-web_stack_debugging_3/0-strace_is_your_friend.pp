# Solve a 500 internal server error on apache
exec { 'solve apache error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => ['usr/bin/', '/bin', '/usr/sbin']
}
