input_spin = input()
input_ec = input()  # ec - Electric charge
if input_spin == "1/2":
    if input_ec == "-1/3":
        print("Strange Quark")
    elif input_ec == "2/3":
        print("Charm Quark")
    elif input_ec == "-1":
        print("Electron Lepton")
    elif input_ec == "0":
        print("Neutrino Lepton")
elif input_spin == "1" and input_ec == "0":
    print("Photon Boson")
