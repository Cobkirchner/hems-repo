#$path = "C:\Cloudstorage\OneDrive\Studium\Masterarbeit\hems-repo\azure\AzureLogin.ctx"
#Import-AzureRmContext -Path $path

#az login -u christian.obkircher@outlook.com -p f14tomcatCO91

$resourceGroupName = "VirtualMachines"
$VMName = "HyperVContainer"

az vm deallocate --resource-group $resourceGroupName --name $VMName

az vm generalize --resource-group $resourceGroupName --name $VMName

az image create --resource-group $resourceGroupName --name HyperVContainerImage --source $VMName

{
  "id": "/subscriptions/672fd4ac-a7a9-4a21-97fd-d410621c8ff2/resourceGroups/VirtualMachines/providers/Microsoft.Compute/images/Hyper
VContainerImage",
  "location": "eastus",
  "name": "HyperVContainerImage",
  "provisioningState": "Succeeded",
  "resourceGroup": "VirtualMachines",
  "sourceVirtualMachine": {
    "id": "/subscriptions/672fd4ac-a7a9-4a21-97fd-d410621c8ff2/resourceGroups/VirtualMachines/providers/Microsoft.Compute/virtualMac
hines/HyperVContainer",
    "resourceGroup": "VirtualMachines"
  },
  "storageProfile": {
    "dataDisks": [],
    "osDisk": {
      "blobUri": "https://hemsstorage.blob.core.windows.net/hemscontainer/hyperv-container.vhd",
      "caching": "ReadWrite",
      "diskSizeGb": 127,
      "managedDisk": null,
      "osState": "Generalized",
      "osType": "Windows",
      "snapshot": null,
      "storageAccountType": "Standard_LRS"
    }
  },
  "tags": null,
  "type": "Microsoft.Compute/images"
}