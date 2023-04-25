0x0A. Configuration management

Configuration management is the practice of maintaining consistent and reliable configurations of software and hardware systems by using tools and processes to manage and control changes to the system cofigurations over time.

Requirements:
<h1>Installing Puppet</h1>
<p>Puppet is a popular open-source configuration management tool used for automating the provisioning, configuration and management of servers and applications enabling administrators to describe infrastructure as code using declarative languages and provides tools for enforcing and testing that code.</p>

<ul>
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
</ul>

<h2>Installing puppet-lint</h2>
<p>Puppet lint is a command-line tool used for analyzing and testing the syntax and style of Puppet code ensuring code is written in a consistent, readable and mainainalbe manner.</p>

<ul>
gem install puppet-lint
</ul>
