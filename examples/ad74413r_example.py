import adi

ad74413r = adi.ad74413r(uri="ip:analog")

print("Voltage Channels")
for i in range(len(ad74413r.voltage_channels)):
    print(f"{ad74413r.voltage_channel_names[i]}")
    print(f"offset:                         {ad74413r.voltage_channels[i].offset}")
    print(f"raw:                            {ad74413r.voltage_channels[i].raw}")
    print(f"sampling_frequency:             {ad74413r.voltage_channels[i].sampling_frequency}")
    print(f"sampling_frequency_available:   {ad74413r.voltage_channels[i].sampling_frequency_available}")
    print(f"scale:                          {ad74413r.voltage_channels[i].scale}\n")

print("Current Channels")
for i in range(len(ad74413r.current_channels)):
    print(f"{ad74413r.current_channel_names[i]}")
    print(f"offset:                         {ad74413r.current_channels[i].offset}")
    print(f"raw:                            {ad74413r.current_channels[i].raw}")
    print(f"sampling_frequency:             {ad74413r.current_channels[i].sampling_frequency}")
    print(f"sampling_frequency_available:   {ad74413r.current_channels[i].sampling_frequency_available}")
    print(f"scale:                          {ad74413r.current_channels[i].scale}\n")