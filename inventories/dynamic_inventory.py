#!/usr/bin/env python

import json
import sys

def main():
    inventory = {
        "_meta": {
            "hostvars": {
                "ansible_host": "localhost",
                "ansible_python_interpreter": sys.executable
            }
        }
    }

    print(json.dumps(inventory, indent=2)

if __name__ == "__main__":
    main()
