$destinationVhd = "https://hemsstorage.blob.core.windows.net/hemscontainer/hyperv-container.vhd"

$vmConfig = New-AzureRmVMConfig -VMName "HyperVContainer" -VMSize "Standard_D4_v3"

$vmConfig = Set-AzureRmVMOSDisk -VM $vmConfig -Name "HyperVContainer" -VhdUri $destinationVhd -CreateOption Attach -Windows

$vmConfig = Add-AzureRmVMNetworkInterface -VM $vmConfig -Id $networkInterface.Id

$vm = New-AzureRmVM -VM $vmConfig -Location $locationName -ResourceGroupName $resourceGroupName