# provider "azurerm" {
#   subscription_id = "672fd4ac-a7a9-4a21-97fd-d410621c8ff2"
#   client_id       = "d51b8d63-6492-4ec0-b994-d0ccdc43555a"
#   client_secret   = "1d068e73-195f-49e3-b553-1f4a4b5e2496"
#   tenant_id       = "ba5e6b38-2d31-46a5-8554-b9d0961b048c"
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
  name                = ["${element(var.hostname.*, count.index)}nic"]
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.rg.name}"

  ip_configuration {
    name                          = ["${element(var.hostname.*, count.index)}ipconfig"]
    subnet_id                     = "${azurerm_subnet.subnet.id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${azurerm_public_ip.pip.id}"
  }
}

resource "azurerm_public_ip" "pip" {
  name                         = ["${element(var.hostname.*, count.index)}-ip"]
  location                     = "${var.location}"
  resource_group_name          = "${azurerm_resource_group.rg.name}"
  public_ip_address_allocation = "Dynamic"
  domain_name_label            = ["${element(var.hostname.*, count.index)}]
}

resource "azurerm_virtual_machine" "vm" {
  name                  = ["${element(var.hostname.*, count.index)}]
  location              = "${var.location}"
  resource_group_name   = "${azurerm_resource_group.rg.name}"
  vm_size               = "${var.vm_size}"
  network_interface_ids = ["${azurerm_network_interface.nic.id}"]

  storage_os_disk {
    name          = ["${element(var.hostname.*, count.index)}-osdisk1"
    image_uri     = "${var.image_uri}"
    vhd_uri       = "https://hemsstorage.blob.core.windows.net/hemscontainer/hyperv-container.vhd"
    os_type       = "${var.os_type}"
    caching       = "ReadWrite"
    create_option = "FromImage"
  }

  os_profile {
    computer_name  = ["${element(var.hostname.*, count.index)}"]
    admin_username = "${var.admin_username}"
    admin_password = "${var.admin_password}"
  }

  os_profile_linux_config {
    disable_password_authentication = false
    }
  # This will create 4 instances
  count = 4  
}