from PyAndroid import PyAndroid as PA
# if you install via pypi use code above, else use import PyAndroid as PA
import os
# Made for pyandroid >= 1.0 <= 1.0.3
os.system('clear') # clear the screen
PA.min_sdk(14) # set minimum api level to run script
print('You have android {} {}, with api {}.\n'.format(PA.android_version(), PA.android_name(), PA.sdk_version()))
print('Your device is {} {}, with machine {}.\n\nYou have {} MB of ram.\n\nYour device was created {}. \n'.format(PA.device_brand(), PA.device_model(), PA.processor_machine(), PA.ram_total('MB'), PA.device_time())) 
print('You run script on {} application.\n'.format(PA.program()) )