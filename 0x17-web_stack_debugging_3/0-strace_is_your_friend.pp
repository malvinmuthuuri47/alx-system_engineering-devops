$file_path = '/var/www/html/wp-settings.php'

# Read the file content
$file_content = file($file_path)

# Replace the extension
$file_content_new = regsubst($file_content, '\.phpp', '.php')

# Write the updated content back to the file
file { $file_path:
  content => $file_content_new,
}
