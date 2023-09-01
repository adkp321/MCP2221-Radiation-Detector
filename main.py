#
# Adam Peterson
#
import hid
import os
import board
import analogio
import time


def loop():
    diode = analogio.AnalogIn(board.G3)

    while True:
        raw = diode.value
        volts = get_voltage(raw)
        print("raw = {:5d} volts = {:5.2f}".format(raw, volts))
        time.sleep(0.5)


def get_voltage_g1():
    v = analogio.AnalogIn(board.G1)
    raw = v.value
    voltage = get_voltage(raw)
    return raw, voltage


def get_voltage_g2():
    v = analogio.AnalogIn(board.G2)
    raw = v.value
    voltage = get_voltage(raw)
    return raw, voltage


def get_voltage_g3():
    v = analogio.AnalogIn(board.G3)
    raw = v.value
    voltage = get_voltage(raw)
    return raw, voltage


def set_dac_voltage_g2(voltage):
    dac = analogio.AnalogOut(board.G2)
    dac.value = voltage


def set_dac_voltage_g3(voltage):
    dac = analogio.AnalogOut(board.G3)
    while True:
        dac.value = voltage


def get_raw(voltage):
    return (voltage*65536)/5


def get_voltage(raw):
    return (raw*5)/65536


def connection_status():

    print(hid.enumerate())
    print('device' in dir(hid))
    device = hid.device()
    device.open(0x04D8, 0x00DD)
    device.close()
    print(os.environ["BLINKA_U2IF"])
    print(dir(board))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connection_status()
    # print(get_voltage_g1())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
