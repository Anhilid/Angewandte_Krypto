# Installing apache2

```sh
sudo apt update
sudo apt install apache2
```

HTML contents are located in `/var/www/html`
Host file is located in `/etc/apache2/sites-enabled/000-default.conf`

# Creating new host
## Create new folder
```sh
sudo mkdir /var/www/gci
```
## Create & edit index file
```sh
cd /var/www/gci/
nano index.html
```

## Setting up VirtualHost config
```sh
cd /etc/apache2/sites-available/
sudo cp 000-default.conf gci.conf # Copying default config
sudo nano gci.conf
```
# Update config
```
ServerAdmin yourname@example.com
DocumentRoot /var/www/gci/
ServerName gci.example.com
```
- **ServerAdmin**: Adress to contact when encountering an error
- **DocumentRoot**: Points to directory of host files
- **ServerName**: Hostname to apply directives to
# Enable VirtualHost
```sh
sudo a2ensite gci.conf # enable host
service apache2 reload # reload apache2 to apply changes
```