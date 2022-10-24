import adi

ad74413r = adi.ad74413r(uri="ip:analog")

print("Voltage Input Channels")
for chan_name, chan in ad74413r.voltage_input_channels.items():
    print(f"id:{chan_name}")
    print(f"offset:                         {chan.offset}")
    print(f"raw:                            {chan.raw}")
    print(f"sampling_frequency:             {chan.sampling_frequency}")
    print(f"sampling_frequency_available:   {chan.sampling_frequency_available}")
    print(f"scale:                          {chan.scale}\n")

print("Voltage Output Channels")
for chan_name, chan in ad74413r.voltage_output_channels.items():
    print(f"id:{chan_name}")
    print(f"raw:    {chan.raw}")
    print(f"scale:  {chan.scale}\n")

print("Current Input Channels")
for chan_name, chan in ad74413r.current_input_channels.items():
    print(f"id:{chan_name}")
    print(f"offset:                         {chan.offset}")
    print(f"raw:                            {chan.raw}")
    print(f"sampling_frequency:             {chan.sampling_frequency}")
    print(f"sampling_frequency_available:   {chan.sampling_frequency_available}")
    print(f"scale:                          {chan.scale}\n")

print("Current Input Channels")
for chan_name, chan in ad74413r.current_output_channels.items():
    print(f"id:{chan_name}")
    print(f"raw:                            {chan.raw}")
    print(f"scale:                          {chan.scale}\n")

ad74413r.voltage_input_channels["voltage1"].sampling_frequency = 4800
print(ad74413r.voltage_input_channels["voltage1"].sampling_frequency)