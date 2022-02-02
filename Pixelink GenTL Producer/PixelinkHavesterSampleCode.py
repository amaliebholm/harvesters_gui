#




# Import Harvester:
from harvesters.core import Harvester
from harvesters.util.pfnc import mono_location_formats, rgb_formats, bgr_formats, rgba_formats, bgra_formats
from PIL import Image
from skimage.io import imsave
import numpy as np

# Create a Harvester object:
h = Harvester()

# Load a GenTL Producer; you can load many more if you want to:
h.add_file('C:/PixeLink/Trunk/host/GenICam/Producer-SourceCode/TLpixelink64/x64/Debug/TLpixelink64_debug.cti')
#h.add_file('C:/Users/smassad.PIXELINK/AppData/Local/Programs/Python/Python37/Lib/site-packages/genicam/TLSimu.cti')

# Enumerate the available devices that GenTL Producers can handle:
h.update()

# Select a target device and create an ImageAcquire object that
# controls the device:
ia = h.create_image_acquirer(0)


#### READ DEVICE CONTROLS ####
print('DeviceVendorName:' + format(ia.remote_device.node_map.DeviceVendorName.value))
print('DeviceModelName:' + format(ia.remote_device.node_map.DeviceModelName.value))
print('DeviceManufacturerInfo:' + format(ia.remote_device.node_map.DeviceManufacturerInfo.value))
print('DeviceVersion:' + format(ia.remote_device.node_map.DeviceVersion.value))
print('DeviceSFNCVersionMajor:' + format(ia.remote_device.node_map.DeviceSFNCVersionMajor.value))
print('DeviceSFNCVersionMinor:' + format(ia.remote_device.node_map.DeviceSFNCVersionMinor.value))
print('DeviceSFNCVersionSubMinor:' + format(ia.remote_device.node_map.DeviceSFNCVersionSubMinor.value))
print('DeviceID:' + format(ia.remote_device.node_map.DeviceID.value))
print('DeviceUserID:' + format(ia.remote_device.node_map.DeviceUserID.value))
print('DeviceTemperatureSelector:' + format(ia.remote_device.node_map.DeviceTemperatureSelector.value))
print('DeviceTemperature:' + format(ia.remote_device.node_map.DeviceTemperature.value))
print('DeviceLinkThroughputLimitMode:' + format(ia.remote_device.node_map.DeviceLinkThroughputLimitMode.value))
print('DeviceLinkThroughputLimit:' + format(ia.remote_device.node_map.DeviceLinkThroughputLimit.value))
print('DeviceMaxThroughput:' + format(ia.remote_device.node_map.DeviceMaxThroughput.value))

#### WRITE DEVICE CONTROLS ####
#ia.remote_device.node_map.DeviceReset.execute()
#ia.remote_device.node_map.DeviceLinkThroughputLimitMode.value = 'On'
#ia.remote_device.node_map.DeviceLinkThroughputLimitMode.value = 'Off'
#ia.remote_device.node_map.DeviceLinkThroughputLimit.value = 1000


#### READ IMAGE FORMAT CONTROLS ####
print('SensorWidth:' + format(ia.remote_device.node_map.SensorWidth.value))
print('SensorHeight:' + format(ia.remote_device.node_map.SensorHeight.value))
print('Width:' + format(ia.remote_device.node_map.Width.value))
print('Height:' + format(ia.remote_device.node_map.Height.value))
print('OffsetX:' + format(ia.remote_device.node_map.OffsetX.value))
print('OffsetY:' + format(ia.remote_device.node_map.OffsetY.value))
print('BinningHorizontal:' + format(ia.remote_device.node_map.BinningHorizontal.value))
print('BinningVertical:' + format(ia.remote_device.node_map.BinningVertical.value))
print('DecimationHorizontal:' + format(ia.remote_device.node_map.DecimationHorizontal.value))
print('DecimationVertical:' + format(ia.remote_device.node_map.DecimationVertical.value))
print('PixelFormat:' + format(ia.remote_device.node_map.PixelFormat.value))
print('PixelSize:' + format(ia.remote_device.node_map.PixelSize.value))
print('PixelColorFilter:' + format(ia.remote_device.node_map.PixelColorFilter.value))

#### WRITE IMAGE FORMAT CONTROLS ####
#ia.remote_device.node_map.Width.value = 1000
#ia.remote_device.node_map.Height.value = 1000
#ia.remote_device.node_map.OffsetX.value = 256
#ia.remote_device.node_map.OffsetY.value = 256
#ia.remote_device.node_map.BinningHorizontal.value = 2
#ia.remote_device.node_map.BinningVertical.value = 2
#ia.remote_device.node_map.DecimationHorizontal.value = 2
#ia.remote_device.node_map.DecimationVertical.value = 2
#ia.remote_device.node_map.PixelFormat.value = 'Mono8'
#ia.remote_device.node_map.PixelFormat.value = 'Mono12g'
#ia.remote_device.node_map.PixelFormat.value = 'Mono16'
#ia.remote_device.node_map.PixelFormat.value = 'BayerRG8'
#ia.remote_device.node_map.PixelFormat.value = 'BayerRG12g'
#ia.remote_device.node_map.PixelFormat.value = 'BayerRG16'
#ia.remote_device.node_map.PixelFormat.value = 'RGB8'
#ia.remote_device.node_map.PixelFormat.value = 'BGR8'
#ia.remote_device.node_map.PixelFormat.value = 'YCbCr422_8'
#ia.remote_device.node_map.PixelFormat.value = 'YCbCr422_8_CbYCrY'


#### READ ACQUISION CONTROLS #### 
print('AcquisitionFrameRate:' + format(ia.remote_device.node_map.AcquisitionFrameRate.value))
print('ExposureTime:' + format(ia.remote_device.node_map.ExposureTime.value))
print('ExposureAuto:' + format(ia.remote_device.node_map.ExposureAuto.value))

#ia.remote_device.node_map.AcquisitionFrameRate.value = 10
#ia.remote_device.node_map.ExposureTime.value = 20000
#ia.remote_device.node_map.ExposureAuto.value = 'Off'
#ia.remote_device.node_map.ExposureAuto.value = 'Once'
#ia.remote_device.node_map.ExposureAuto.value = 'Continuous'



#### READ ANALOG CONTROLS #### 
print('Gain:' + format(ia.remote_device.node_map.Gain.value))
#color only
#print('BalanceRatioSelector:' + format(ia.remote_device.node_map.BalanceRatioSelector.value))
#color only
##print('BalanceRatio:' + format(ia.remote_device.node_map.BalanceRatio.value))
#color only
##print('BalanceWhiteAuto:' + format(ia.remote_device.node_map.BalanceWhiteAuto.value))
print('Gamma:' + format(ia.remote_device.node_map.Gamma.value))
print('LUTEnable:' + format(ia.remote_device.node_map.LUTEnable.value))
print('LUTIndex:' + format(ia.remote_device.node_map.LUTIndex.value))
print('LUTValue:' + format(ia.remote_device.node_map.LUTValue.value))


#### WRTIE ANALOG CONTROLS #### 
#ia.remote_device.node_map.Gain.value = 12
#ia.remote_device.node_map.BalanceRatioSelector.value = 'Red'
#ia.remote_device.node_map.BalanceRatioSelector.value = 'Green'
#ia.remote_device.node_map.BalanceRatioSelector.value = 'Blue'
#ia.remote_device.node_map.BalanceRatio.value = 1.2
#ia.remote_device.node_map.BalanceWhiteAuto.value = 'Off'
#ia.remote_device.node_map.BalanceWhiteAuto.value = 'Once'
#ia.remote_device.node_map.Gamma.value = 2.2
#ia.remote_device.node_map.LUTEnable.value = True
#ia.remote_device.node_map.LUTEnable.value = False
#ia.remote_device.node_map.LUTIndex.value = 50
#ia.remote_device.node_map.LUTValue.value = 128


#### READ TRANSPORT LAYER CONTROLS #### 
print('PayloadSize:' + format(ia.remote_device.node_map.PayloadSize.value))


#### READ GPIO CONTROLS #### 
print('GPIOSelector:' + format(ia.remote_device.node_map.GPIOSelector.value))
print('GPIOEnable:' + format(ia.remote_device.node_map.GPIOEnable.value))
print('GPIOModeSelector:' + format(ia.remote_device.node_map.GPIOModeSelector.value))
print('GPIOPolaritySelector:' + format(ia.remote_device.node_map.GPIOPolaritySelector.value))
print('GPIOParameterOne:' + format(ia.remote_device.node_map.GPIOParameterOne.value))
print('GPIOParameterTwo:' + format(ia.remote_device.node_map.GPIOParameterTwo.value))
print('GPIOParameterThree:' + format(ia.remote_device.node_map.GPIOParameterThree.value))

#### WRITE GPIO CONTROLS #### 
#ia.remote_device.node_map.GPIOSelector.value = 'GPIO1'
#ia.remote_device.node_map.GPIOSelector.value = 'GPIO2'
#ia.remote_device.node_map.GPIOSelector.value = 'GPIO3'
#ia.remote_device.node_map.GPIOEnable.value = True
#ia.remote_device.node_map.GPIOModeSelector.value = 'Strobe'
#ia.remote_device.node_map.GPIOModeSelector.value = 'Normal'
#ia.remote_device.node_map.GPIOModeSelector.value = 'Pulse'
#ia.remote_device.node_map.GPIOModeSelector.value = 'Busy'
#ia.remote_device.node_map.GPIOModeSelector.value = 'Flash'
#ia.remote_device.node_map.GPIOPolaritySelector.value = 'Positive'
#ia.remote_device.node_map.GPIOPolaritySelector.value = 'Negative'
#ia.remote_device.node_map.GPIOParameterOne.value = 0
#ia.remote_device.node_map.GPIOParameterTwo.value = 0
#ia.remote_device.node_map.GPIOParameterThree.value = 0


#### READ TRIGGER CONTROLS ####
print('TriggerEnable:' + format(ia.remote_device.node_map.TriggerEnable.value))
print('TriggerModeSelector:' + format(ia.remote_device.node_map.TriggerModeSelector.value))
print('TriggerTypeSelector:' + format(ia.remote_device.node_map.TriggerTypeSelector.value))
print('TriggerPolaritySelector:' + format(ia.remote_device.node_map.TriggerPolaritySelector.value))
print('Delay:' + format(ia.remote_device.node_map.Delay.value)) 

#### WRITE TRIGGER CONTROLS ####
#ia.remote_device.node_map.TriggerEnable.value = True
#ia.remote_device.node_map.TriggerModeSelector.value = 'TriggerMode0'
#ia.remote_device.node_map.TriggerModeSelector.value = 'TriggerMode1'
#ia.remote_device.node_map.TriggerModeSelector.value = 'TriggerMode14'
#ia.remote_device.node_map.TriggerPolaritySelector.value = 'Negative'
#ia.remote_device.node_map.TriggerPolaritySelector.value = 'Positive'
#ia.remote_device.node_map.TriggerTypeSelector.value = 'Software'
#ia.remote_device.node_map.TriggerTypeSelector.value = 'Hardware'
#ia.remote_device.node_map.Delay.value = 0


#### READ USER SET CONTROLS ####
print('UserSetSelector:' + format(ia.remote_device.node_map.UserSetSelector.value))

#### WRITE USER SET CONTROLS ####
#ia.remote_device.node_map.UserSetSelector.value = 'Default'
#ia.remote_device.node_map.UserSetSelector.value = 'UserSet1'
#ia.remote_device.node_map.UserSetLoad.execute()
#ia.remote_device.node_map.UserSetSave.execute()


#### READ PIXELINK FEATURES ####
#color only
##print('PxLSaturation:' + format(ia.remote_device.node_map.PxLSaturation.value))
#color only
#print('PxLColorTemperature:' + format(ia.remote_device.node_map.PxLColorTemperature.value))
print('PxLMaxPixelSize:' + format(ia.remote_device.node_map.PxLMaxPixelSize.value))
print('PxLNumKneepoints:' + format(ia.remote_device.node_map.PxLNumKneepoints.value))
print('PxLSsMaxValue:' + format(ia.remote_device.node_map.PxLSsMaxValue.value))
print('PxLLinkThroughputTarget:' + format(ia.remote_device.node_map.PxLLinkThroughputTarget.value))
print('PxLNumGpos:' + format(ia.remote_device.node_map.PxLNumGpos.value))
print('PxLAcquisitionFrameRateAuto:' + format(ia.remote_device.node_map.PxLAcquisitionFrameRateAuto.value))
print('PxLGammaEnable:' + format(ia.remote_device.node_map.PxLGammaEnable.value))
print('PxLAutoRoiEnable:' + format(ia.remote_device.node_map.PxLAutoRoiEnable.value))
print('PxLAutoRoiWidth:' + format(ia.remote_device.node_map.PxLAutoRoiWidth.value))
print('PxLAutoRoiHeight:' + format(ia.remote_device.node_map.PxLAutoRoiHeight.value))
print('PxLAutoRoiOffsetX:' + format(ia.remote_device.node_map.PxLAutoRoiOffsetX.value))
print('PxLAutoRoiOffsetY:' + format(ia.remote_device.node_map.PxLAutoRoiOffsetY.value))
print('PxLAutoExposureMin:' + format(ia.remote_device.node_map.PxLAutoExposureMin.value))
print('PxLAutoExposureMax:' + format(ia.remote_device.node_map.PxLAutoExposureMax.value))
print('PxLCameraHDREnable:' + format(ia.remote_device.node_map.PxLCameraHDREnable.value))
print('PxLInterleavedHDREnable:' + format(ia.remote_device.node_map.PxLInterleavedHDREnable.value))

#### WRITE PIXELINK FEATURES ####
#ia.remote_device.node_map.PxLSaturation.value = 140
#ia.remote_device.node_map.PxLColorTemperature.value = 6500
#ia.remote_device.node_map.PxLDeviceReconfigure.execute()
#ia.remote_device.node_map.PxLAcquisitionFrameRateAuto.value = 'Off'
#ia.remote_device.node_map.PxLAcquisitionFrameRateAuto.value = 'Continuous'
#ia.remote_device.node_map.PxLGammaEnable.value = True
#ia.remote_device.node_map.PxLAutoRoiEnable.value = True
#ia.remote_device.node_map.PxLAutoRoiWidth.value = 1000
#ia.remote_device.node_map.PxLAutoRoiHeight.value = 1000
#ia.remote_device.node_map.PxLAutoRoiOffsetX.value = 256
#ia.remote_device.node_map.PxLAutoRoiOffsetY.value = 256
#ia.remote_device.node_map.PxLAutoExposureMin.value = 10000
#ia.remote_device.node_map.PxLAutoExposureMax.value = 100000
#ia.remote_device.node_map.PxLCameraHDREnable.value = True
#ia.remote_device.node_map.PxLInterleavedHDREnable.value = True


# Allow the ImageAcquire object to start image acquisition: 
ia.start_acquisition()

# We are going to fetch a buffer filled up with an image:
# Note that you'll have to queue the buffer back to the
# ImageAcquire object once you consumed the buffer; the
# with statement takes care of it on behalf of you:
with ia.fetch_buffer() as buffer:

	# Let's create an alias of the 2D image component; it can be
	# lengthy which is not good for typing. In addition, note that
	# a 3D camera can give you 2 or more components:
	component = buffer.payload.components[0]
	payload = buffer.payload
	component = payload.components[0]
	width = component.width
	height = component.height
	data_format = component.data_format
	
	print(data_format)

	_1d = component.data
	print(_1d)
	

	if data_format == 'Mono8':
	
		content = component.data.reshape(height, width)
		im = Image.fromarray(content)
		im.save('result.png')
	
	elif data_format == 'BayerRG8':
		
		ow, oh = width//2, height//2

		bayer = component.data.reshape(height, width)

		
	
		# Pick up raw uint8 samples
		G0  = bayer[1::2, 0::2]     # rows 1,3,5,7 columns 0,2,4,6
		G1  = bayer[0::2, 1::2]     # rows 0,2,4,6 columns 1,3,5,7
		R = bayer[0::2, 0::2]     # rows 0,2,4,6 columns 0,2,4,6
		B = bayer[1::2, 1::2]     # rows 1,3,5,7 columns 1,3,5,7

		
	
		# Chop any left-over edges and average the 2 Green values
		R = R[:oh,:ow]
		B = B[:oh,:ow]
		G = G0[:oh,:ow]//2 + G1[:oh,:ow]//2

		
	
		# Formulate image by stacking R, G and B and save
		out = np.dstack((R,G,B)) 
		imsave('result.png',out)




# Stop the ImageAcquier object acquiring images:
ia.stop_acquisition()

# We're going to leave here shortly:
ia.destroy()
h.reset()

