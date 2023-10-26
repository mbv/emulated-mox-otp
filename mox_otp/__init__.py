"""
MOX OTP python package
"""

import os

__version__ = '0.4.0'


# hash algorithm used for message signature
HASH_TYPE = "sha512"

SYSFS_ROOT_NEW = "/usr/local/turris-mox"
DEBUGFS_ROOT_NEW = "/usr/local/turris-mox"

SYSFS_ROOT = SYSFS_ROOT_NEW
PUBKEY_FILENAME = "pubkey"
SERIAL_FILENAME = "serial_number"
MAC_FILENAME = "mac_address1"

PUBKEY_PATH = os.path.join(SYSFS_ROOT, PUBKEY_FILENAME)
SERIAL_PATH = os.path.join(SYSFS_ROOT, SERIAL_FILENAME)
MAC_PATH = os.path.join(SYSFS_ROOT, MAC_FILENAME)
