# Reboot raspberry on connection lost

If the internet connection is lost for one hour, the raspberry will reboot. You pass a custom timeout (in seconds) as an argument for the command.

This script is required in case the 3G goes down.

# Execution

* `# reboot_on_connection_lost`
* `# reboot_on_connection_lost <DELAY_FOR_REBOOT> <FREQUENCY_OF_CHECK>` 
