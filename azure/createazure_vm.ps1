﻿$path = "C:\Cloudstorage\OneDrive\Studium\Masterarbeit\hems-repo\azure\AzureLogin.ctx"
Import-AzureRmContext -Path $path

$resourceGroupName = "VirtualMachines"
$virtualNetworkName = "vm-network"
$locationName = "eastus"
$virtualNetwork = Get-AzureRmVirtualNetwork -ResourceGroupName $resourceGroupName -Name $virtualNetworkName


$publicIp = New-AzureRmPublicIpAddress -Name "HyperVPIP2" -ResourceGroupName $ResourceGroupName -Location $locationName -AllocationMethod Dynamic
$networkInterface = New-AzureRmNetworkInterface -ResourceGroupName $resourceGroupName -Name "HyperVNIC2" -Location $locationName -SubnetId $virtualNetwork.Subnets[0].Id -PublicIpAddressId $publicIp.Id


#Standard_D4_v3

$destinationVhd = "https://hemsstorage.blob.core.windows.net/hemscontainer/hyperv-container2.vhd"

$vmConfig = New-AzureRmVMConfig -VMName "HyperVContainer2" -VMSize "Standard_D4_v3"

$vmConfig = Set-AzureRmVMOSDisk -VM $vmConfig -Name "HyperVContainer2" -VhdUri $destinationVhd -CreateOption Attach -Windows

$vmConfig = Add-AzureRmVMNetworkInterface -VM $vmConfig -Id $networkInterface.Id

$vm = New-AzureRmVM -VM $vmConfig -Location $locationName -ResourceGroupName $resourceGroupName