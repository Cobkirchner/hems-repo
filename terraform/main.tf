# provider "azurerm" {
#   subscription_id = "672fd4ac-a7a9-4a21-97fd-d410621c8ff2"
#   client_id       = "753f0f23-ba36-4d70-b6f7-894904d650e2"
#   client_secret   = "75d13d44-66f6-4256-9cc0-103610879df6"
#   tenant_id       = "ba5e6b38-2d31-46a5-8554-b9d0961b048c""
# }

 

resource "azurerm_resource_group" "rg" {
  name     = "${var.resource_group}"
  location = "${var.location}"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "${var.hostname}vnet"
  location            = "${var.location}"
  address_space       = ["${var.address_space}"]
  resource_group_name = "${azurerm_resource_group.rg.name}"
}

resource "azurerm_subnet" "subnet" {
  name                 = "${var.hostname}subnet"
  virtual_network_name = "${azurerm_virtual_network.vnet.name}"
  resource_group_name  = "${azurerm_resource_group.rg.name}"
  address_prefix       = "${var.subnet_prefix}"
}

resource "azurerm_network_interface" "nic" {
  count               = "${var.instance_count}"  
  name                = "hypervcontainer-nic${count.index}"
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.rg.name}"

  ip_configuration {
    name                          = "hypervcontainer-ipconfig${count.index}"
    subnet_id                     = "${azurerm_subnet.subnet.id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${element(azurerm_public_ip.pip.*.id, count.index)}"
  }
}

resource "azurerm_public_ip" "pip" {
  count               = "${var.instance_count}"  
  name                         = "hypervcontainer-pip${count.index}"
  location                     = "${var.location}"
  resource_group_name          = "${azurerm_resource_group.rg.name}"
  public_ip_address_allocation = "Dynamic"
  domain_name_label            = "hypervcontainer-pip${count.index}"
}


resource "azurerm_virtual_machine" "vm" {
  count               = "${var.instance_count}"
  name                  = "hypervcontainer-${count.index}"
  location              = "${var.location}"
  resource_group_name   = "${azurerm_resource_group.rg.name}"
  vm_size               = "${var.vm_size}"
  network_interface_ids = ["${element(azurerm_network_interface.nic.*.id, count.index)}"]

    storage_os_disk {  
    name          = "hypervcontainer-osdisk${count.index}"
    image_uri     = "${var.image_uri}"
    vhd_uri       = "https://hemsstorage.blob.core.windows.net/hemscontainer/hyperv-container2.vhd"
    os_type       = "${var.os_type}"
    caching       = "ReadWrite"
    create_option = "FromImage"
  }

  os_profile {  
    computer_name  = "hypervcontainer-${count.index}"
    admin_username = "${var.admin_username}"
    admin_password = "${var.admin_password}"
  }

  os_profile_linux_config {
    disable_password_authentication = false
  }


}