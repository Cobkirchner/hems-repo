output "hostname" {
  value = "${var.hostname}"
}

output "vm_fqdn" {
  value = "${azurerm_public_ip.pip.*.id}"
}

output "ssh_command" {
  value = "${concat("ssh ", var.admin_username, "@", azurerm_public_ip.pip.*.id)}"
}