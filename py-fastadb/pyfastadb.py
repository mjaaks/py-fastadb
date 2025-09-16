import subprocess
import time
import shutil

class Client:
    def __init__(self, adb_path=None, fast_path=None):
        self._adb_path = adb_path or shutil.which('adb') or None
        self._fast_path = fast_path or shutil.which('fastboot') or None
        if self._adb_path is None:
            print("Error")
            ## throw error
        if self._fast_path is None:
            print("Error")
            ## throw error

    def get_adb_devices(self):
        res = subprocess.run([self._adb_path, "devices"], capture_output=True, text=True)
        dev = []
        res = res.stdout.splitlines()
        for i in res[1:]:
            i = i.strip().split()
            if len(i) >= 2:
                dev.append((i[0], i[1]))
        return dev or None

    def wait_for(self, device_serial, wait_type="device"):

        if type(device_serial) == AdbDevice:
            device_serial = device_serial.serial

        if wait_type != "bootloader" and wait_type != "fastboot":
            subprocess.run([self._adb_path, "-s", device_serial, f"wait-for-{wait_type}"], capture_output=True, text=True)
        else:
            while True:
                res = subprocess.run([self._adb_path, "-s", device_serial], capture_output=True, text=True).stdout.splitlines()
                for i in res:
                    if i.strip().split()[0] == device_serial:
                        break
                time.sleep(0.75)


class AdbDevice:
    def __init__(self, client: Client, serial):
        self._adb_path = client._adb_path
        self.serial = serial

    def reboot(self, reboot_type=""):
        subprocess.run([self._adb_path, "-s", self.serial, "reboot", reboot_type], capture_output=True, text=True)